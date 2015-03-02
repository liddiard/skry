import re

from django import template
from django.template.defaultfilters import stringfilter
from django.template import Context
from django.template.loader import get_template

from project.settings.base import MEDIA_URL
from research.models import Image

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def image(value):
    img_re = r'\[img(?P<pk>\d+)\]'
    return re.sub(img_re, imgHTML, value)

def imgHTML(match):
    try:
        image = Image.objects.get(pk=match.group('pk'))
    except Image.DoesNotExist:
        return "" # fail silently
    template = get_template('research/inc/image.html')
    context = Context({'image': image})
    return template.render(context)
