from django import template
from django.template.defaultfilters import stringfilter
import urllib

register = template.Library()
@register.filter(name="unquote")
@stringfilter
def unquote(value):
    return urllib.unquote(value)

