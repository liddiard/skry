from rest_framework import serializers

from attachments import serializers as attachments_serializers
from authors import serializers as authors_serializers
from display import serializers as display_serializers
from organization import serializers as organization_serializers
from sports import serializers as sports_serializers
from . import models
from . import utils


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Status


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
