import inspect

from rest_framework import serializers
from django.db.models.fields import Field
from django.contrib.contenttypes.models import ContentType

from attachments import serializers as attachments_serializers
from authors import serializers as authors_serializers
from display import serializers as display_serializers
from organization import serializers as organization_serializers
from sports import serializers as sports_serializers
from . import models
from . import utils


def schema_serializer(request):
    """Serializes the current Django project's schema (apps, models, and model
    fields) into a Python dictionary suitable for JSON serialization and
    checks which models the passed user can create/update/delete.
    """

    apps = []
    # iterate through a list of all installed apps once. the content
    # types table is structured like so:
    #
    #  id |  app_label   |        model
    # ----+--------------+---------------------
    #   1 | admin        | logentry
    #   2 | auth         | permission
    #   3 | auth         | group
    #   4 | auth         | user
    #
    # so the code below selects rows with a distinct app label and forms
    # a list of the app label names and a models list which will be
    # populated later. NOTE: the line below only works with a PostgreSQL
    # backend; cf.
    # https://docs.djangoproject.com/en/1.8/ref/models/querysets/#distinct
    for content_type in ContentType.objects.distinct('app_label'):
        apps.append({
            'name': content_type.app_label,
            'models': []
        })

    for app in apps:
        app_name = app['name']
        # get the content types associated with this app
        app_content_types = ContentType.objects\
                                       .filter(app_label=app_name)

        for content_type in app_content_types:
            # get the model object represented by this content type
            # https://docs.djangoproject.com/en/1.8/ref/contrib/contenttypes/#django.contrib.contenttypes.models.ContentType.model_class
            model_name = content_type.model
            model = content_type.model_class()
            user = request.user
            app['models'].append({
                # camel-cased name of the model
                # http://stackoverflow.com/a/6572002/2487925
                'name': model._meta.object_name,
                'content_type_id': content_type.id,
                'verbose_name': model._meta.verbose_name.title(),
                'verbose_name_plural': model._meta.verbose_name_plural.title(),
                'url': utils.reverse_url(model_name, request),
                'permissions': {
                    'add': utils.has_perm(user, app_name, model_name, 'add'),
                    'change': utils.has_perm(user, app_name, model_name,
                                             'change'),
                    'delete': utils.has_perm(user, app_name, model_name,
                                             'delete')
                },
                'fields': []
            })

            # iterate through all fields, including relations
            # https://docs.djangoproject.com/en/1.8/ref/models/meta/#django.db.models.options.Options.get_fields
            for field in model._meta.get_fields():
                # 'fields' key of the last-appended model
                model_fields = app['models'][-1]['fields']

                # check if field is a regular field (NOT a reverse relation)
                if isinstance(field, Field):
                    model_fields.append({
                        # some fields below follow the pattern
                        # "inspect.isclass([field]) or None".
                        # this is because these fields are sometimes
                        # objects, not strings, and thus can't be JSON
                        # serialized without custom serialization.
                        # if a field is an object, we leave it None (null)
                        'name': field.name,
                        'blank': field.blank,
                        'help_text': inspect.isclass(field.help_text) or None,
                        'is_relation': field.is_relation,
                        'relation': utils.get_related_field_model(field),
                        'null': field.null,
                        'primary_key': field.primary_key,
                        'max_length': field.max_length,
                        'verbose_name': field.verbose_name.title(),
                        'choices': field._choices,
                        'limit_choices_to': utils.get_limit_chocies_to(field),
                        'editable': field.editable,
                        'type': field.get_internal_type()
                    })

    return apps


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Status
        fields = "__all__"


class BodyTextSerializer(serializers.HyperlinkedModelSerializer):
    """Abstract base class which strips internal comments from an object's
    'body' field and adds a 'body_unsanitized' field for authenticated users.
    """

    body = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super(BodyTextSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.user.is_authenticated():
            # sometimes a serializer is initialized without a request, so we
            # must check for its existence first
            self.fields['body_unsanitized'] = serializers.\
                                              SerializerMethodField()

    def get_body(self, obj):
        return utils.strip_internal_comments(obj.body)

    def get_body_unsanitized(self, obj):
        return obj.body


class StorySerializer(BodyTextSerializer):
    authors = authors_serializers.AuthorSerializer(many=True)
    alternate_template = display_serializers.TemplateSerializer()
    sections = organization_serializers.SectionSerializer(many=True)
    tags = organization_serializers.TagSerializer(many=True)
    card = attachments_serializers.ImageSerializer()
    card_size = display_serializers.CardSizeSerializer()
    featured_image = attachments_serializers.ImageSerializer()
    featured_video = attachments_serializers.VideoSerializer()
    featured_audio = attachments_serializers.AudioSerializer()
    review = attachments_serializers.ReviewSerializer()
    poll = attachments_serializers.PollSerializer()
    game = sports_serializers.GameSerializer()
    is_published = serializers.SerializerMethodField()
    is_breaking = serializers.SerializerMethodField()

    class Meta:
        model = models.Story
        exclude = ('assignment_slug', 'status', 'summary', 'angle', 'sources',
                   'late_run', 'created')

    def __init__(self, *args, **kwargs):
        super(StorySerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.user.is_authenticated():
            # sometimes a serializer is initialized without a request, so we
            # must check for its existence first
            self.fields['assignment_slug'] = serializers.CharField()
            self.fields['status'] = StatusSerializer()
            self.fields['summary'] = serializers.CharField()
            self.fields['angle'] = serializers.CharField()
            self.fields['sources'] = serializers.CharField()
            self.fields['late_run'] = serializers.BooleanField()
            self.fields['created'] = serializers.DateTimeField()

    def get_is_published(self, obj):
        return obj.is_published()

    def get_is_breaking(self, obj):
        return obj.is_breaking()


class PageSerializer(BodyTextSerializer):
    alternate_template = display_serializers.TemplateSerializer()

    class Meta:
        model = models.Page
        fields = "__all__"
