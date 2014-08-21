from django import template
import re

register = template.Library()


@register.filter
def strip_url(value):
    # Remove `http://`, `https://`, `www.` and trailing slash
    return re.search('^(https?://)?(www\.)?(.*?)(/)?$', value).group(3)
