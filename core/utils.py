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

def get_limit_chocies_to(field):
    """Get the limited choices of models to which this field can refer.

    limit_choices_to is used with GenericForeignKeys among other things.
    Returns an empty list if choices are not limited on this field or not
    applicable to this field. More info:
    https://docs.djangoproject.com/en/1.8/ref/models/fields/#django.db.models.ForeignKey.limit_choices_to
    """

    choices = []

    # have to check that both of these attributes are present, in this order
    if field.rel and field.rel.limit_choices_to:

        # This is really confusing, but basically "limit_choices_to" is a Q
        # object
        # (https://docs.djangoproject.com/en/1.8/topics/db/queries/#complex-lookups-with-q-objects).
        # It looks something like this (obtained from the "__dict__"
        # attribute):
        #
        # {'connector': u'OR', 'negated': False, 'children': [<Q: (AND:
        # ('model', 'story'), ('app_label', 'core'))>, <Q: (AND: ('model',
        # 'photorequest'), ('app_label', 'requests'))>, <Q: (AND: ('model',
        # 'graphicrequest'), ('app_label', 'requests'))>, <Q: (AND: ('model',
        # 'illustrationrequest'), ('app_label', 'requests'))>]}
        #
        # We don't really care about this top level; as you can see, all the
        # choices are in the "children" attribute. "children" is a list of Q
        # objects. A single element of it looks like this:
        #
        # {'connector': u'AND', 'negated': False, 'children': [('model',
        # 'story'), ('app_label', 'core')]}
        #
        # Once again, we need to access the "children" attribute to get to
        # the information we care about. This second "children" attribute is
        # a list of regular Python tuples, so we can access individual
        # elements of it using bracket syntax.
        for q_object in field.rel.limit_choices_to.children:
            choices.append({
                'app': q_object.children[1][1],
                'model': q_object.children[0][1]
            })
    return choices

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
