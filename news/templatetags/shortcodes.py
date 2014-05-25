import re

from django import template
from django.template.defaultfilters import stringfilter
from django.template import Context
from django.template.loader import get_template

from project.settings.base import MEDIA_URL
from news.models import Image, Video, Audio

register = template.Library()


@register.filter(is_safe=True)
@stringfilter
def image(value):
    img_re = r'\[img(?P<pk>\d+)\s+(?P<align>\S+)?\]'
    template = get_template('news/inc/image.html')
    return re.sub(img_re, imgHTML, value)

def imgHTML(match):
    try:
        image = Image.objects.get(pk=match.group('pk'))
    except Image.DoesNotExist:
        return "" # fail silently
    align = match.group('align')
    template = get_template('news/inc/image.html')
    context = Context({'image': image, 'align': align})
    return template.render(context)
    

@register.filter(is_safe=True)
@stringfilter
def video(value):
    vd_re = r'\[video(?P<pk>\d+)\s+(?P<align>\S+)?\]'
    return re.sub(vd_re, vdHTML, value)

def vdHTML(match):
    try:
        video = Video.objects.get(pk=match.group('pk'))
    except Video.DoesNotExist:
        return "" # fail silently
    align = match.group('align')
    template = get_template('news/inc/video.html')
    context = Context({'video': video, 'align': align})
    return template.render(context)


@register.filter(is_safe=True)
@stringfilter
def audio(value):
    aud_re = r'\[audio(?P<pk>\d+)\s+(?P<align>\S+)?\]'
    return re.sub(aud_re, audHTML, value)

def audHTML(match):
    try:
        audio = Audio.objects.get(pk=match.group('pk'))
    except Audio.DoesNotExist:
        return "" # fail silently
    align = match.group('align')
    template = get_template('news/inc/audio.html')
    context = Context({'audio': audio, 'align': align, 'MEDIA_URL': MEDIA_URL})
    return template.render(context)


@register.filter(is_safe=True)
@stringfilter
def infobox(value):
    inf_re = r'\[infobox\s+(?P<align>\S+)\](?P<content>.*)\[/infobox\]'
    return re.sub(inf_re, infHTML, value, flags=re.DOTALL)

def infHTML(match):
    align = match.group('align')
    content = match.group('content')
    template = get_template('news/inc/infobox.html')
    context = Context({'content': content, 'align': align})
    return template.render(context)


@register.filter(is_safe=True)
@stringfilter
def all_shortcodes(value):
    return audio(video(image(infobox(value))))
