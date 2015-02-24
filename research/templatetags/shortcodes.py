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
    img_re = r'\[img(?P<pk>\d+)\s+(?P<align>\S+)?\]'
    return re.sub(img_re, imgHTML, value)

def imgHTML(match):
    try:
        image = Image.objects.get(pk=match.group('pk'))
    except Image.DoesNotExist:
        return "" # fail silently
    align = match.group('align')
    template = get_template('research/inc/image.html')
    context = Context({'image': image, 'align': align})
    return template.render(context)


@register.filter(is_safe=True)
@stringfilter
def all_shortcodes(value):
    return image(value)
