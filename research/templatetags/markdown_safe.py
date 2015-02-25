import markdown2

from django import template
from django.utils.safestring import mark_safe


register = template.Library()

@register.filter(is_safe=True)
def markdown_safe(value):
    return markdown2.markdown(value)
