from django import template
import re

register = template.Library()


@register.filter
def strip_url(value):
    # Remove `http://`, `www.` and trailing slash
    return re.search('^(http://)?(www\.)?(.*?)(/)?$', value).group(3)
