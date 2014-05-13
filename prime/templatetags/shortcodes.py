import re
from django import template
from django.template.defaultfilters import stringfilter
from dailybruin.settings.base import MEDIA_URL
from prime.models import Image
register = template.Library()

@register.filter(is_safe=True)
@stringfilter
def image(value):
    img = r'\[img(?P<pk>\d+)\s*(?P<display>\S+)?\]'
    return re.sub(img, imgHTML, value)
    
@register.filter(is_safe=True)
@stringfilter
def youtube(value):
    yt = r'\[youtube\]http://youtu\.be/(?P<uid>\S+)\[/youtube\]'
    return re.sub(yt, ytHTML, value)


def imgHTML(match):
    try:
        image = Image.objects.get(pk=match.group('pk'))
    except Image.DoesNotExist:
        return "" # IDEA: don't fail silently?
    given_display = match.group('display')
    # IDEA: check if given_display is in a list of valid dispaly options.
    # If not, assign it to default value.
    # Would prevent users from assigning any css class they want.
    display = given_display if given_display is not None else "right"
    params = {'display': display,
              'MEDIA_URL': MEDIA_URL,
              'filename': image.image,
              'caption': image.caption
    }
    if image.author:
        params['author'] = image.author
        organization = image.author.organization
        if organization:
            params['organization'] = " / %s" % organization
        else:
            params['organization'] = ""
    else:
        params['organization'] = ""
        params['author'] = ""
    return '''
           <figure class="%(display)s">
               <div class="image">
                   <img src="%(MEDIA_URL)s%(filename)s"/>
                   <div class="credit"><strong>%(author)s</strong>
                       %(organization)s</div>
               </div>
               <figcaption>%(caption)s</figcaption>
           </figure>
           ''' % params

def ytHTML(match):
    uid = match.group('uid')
    return '''
        <iframe width="500" height="281" 
                src="//www.youtube.com/embed/%s" frameborder="0" 
                allowfullscreen></iframe>
           ''' % uid
