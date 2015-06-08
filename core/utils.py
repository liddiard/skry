import re
import json
import inspect

from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.core.urlresolvers import NoReverseMatch
from rest_framework.reverse import reverse


def strip_internal_comments(text):
    """Removes internal comments from a string and normalizes whitespace
    around them.

    Comments are in the format [[comment]]. For example, the string 'Lorem
    ispum [[dolor sit]] amet.' will be transformed to 'Lorem ipsum amet.'
    Further examples: https://www.regex101.com/r/eN0iR4/2
    """

    return re.sub(pattern=r'(\s)?\[\[.*\]\](\s)?', repl=' ', string=text)

def get_related_field_model(field):
    """Returns a field's related field model's app and name or None"""

    if field.rel:
        model = field.rel.to
        return {
            'app': model._meta.app_label,
            'name': model._meta.object_name
        }
    else:
        return None

def reverse_url(model, request):
    """Attempts to reverse a URL using Django Rest Framework's URL reverse
    function.

    Function: http://www.django-rest-framework.org/api-guide/reverse/#reverse
    If URL reversal fails, returns None. 'model' argument should be in the
    lowercased, no-underscore format of the contenttypes framework.
    """
    try:
        return reverse('v1:%s-list' % model, request=request)
    except NoReverseMatch:
        return None

def has_perm(user, app, model, action):
    """Checks is a user has permission to perform an action on a model.

    'app' and 'model' arguments should be in the lowercased, no-underscore
    format of the contenttypes framework. More information here:
    https://docs.djangoproject.com/en/1.8/topics/auth/default/#default-permissions
    """
    return user.has_perm('%s.%s_%s' % (app, action, model))

def project_schema_to_dict(request):
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
                'url': reverse_url(model_name, request),
                'permissions': {
                    'add': has_perm(user, app_name, model_name, 'add'),
                    'change': has_perm(user, app_name, model_name, 'change'),
                    'delete': has_perm(user, app_name, model_name, 'delete')
                },
                'fields': []
            })

            # iterate through all fields, including relations
            # https://docs.djangoproject.com/en/1.8/ref/models/meta/#django.db.models.options.Options.get_fields
            for field in model._meta.get_fields():
                # 'fields' key of the last-appended model
                model_fields = app['models'][-1]['fields']

                # check if field is a regular field (NOT a reverse relation)
                if isinstance(field, models.fields.Field):
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
                        'relation': get_related_field_model(field),
                        'null': field.null,
                        'primary_key': field.primary_key,
                        'max_length': field.max_length,
                        'verbose_name': field.verbose_name.title(),
                        'choices': field._choices,
                        'editable': field.editable,
                        'type': field.get_internal_type()
                    })

    return apps
