import re

from rest_framework.reverse import reverse
from django.core.urlresolvers import NoReverseMatch


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
            'model': model._meta.object_name
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
