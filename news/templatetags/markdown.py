from django import template
from django.utils.safestring import mark_safe
import markdown2
  
register = template.Library()
   
@register.filter()
def markdown(value):
    return mark_safe(markdown2.markdown(value, safe_mode='escape'))
