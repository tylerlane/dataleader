from django import template
from django.template.defaultfilters import stringfilter
import urllib

register = template.Library()
@register.filter(name="url_target_blank")
@stringfilter
def url_target_blank(text):
	#making a href's open in a new page and replacing https links with http
    return text.replace('<a ', '<a target="_blank" ').replace( 'https','http')

url_target_blank.is_safe = True