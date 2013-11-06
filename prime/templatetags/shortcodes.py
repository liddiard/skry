import re
from django import template
from django.template.defaultfilters import stringfilter
from dailybruin.settings.base import MEDIA_URL
from prime.models import Image
register = template.Library()

@register.filter
@stringfilter
def shortcode(value):
    img = r'\[img(\d+)\]'
    return re.sub(img, imgHTML, value)

def imgHTML(match):
    try:
        image = Image.objects.get(pk=match.groups()[0])
    except Image.DoesNotExist:
        return ""
    data = {'MEDIA_URL': MEDIA_URL,
            'filename': image.image,
            'author': image.author,
            'caption': image.caption
    }
    return '''
           <figure>
               <div class="image">
                   <img src="%(MEDIA_URL)s%(filename)s"/>
                   <div class="credit">%(author)s</div>
               </div>
               <figcaption>%(caption)s</figcaption>
           </figure>
           ''' % data
