from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.tag
def breadcrumb(parser, token):
    args = token.split_contents()
    values = [parser.compile_filter(arg) for arg in args[1:]]
    return NameNode(values)


class NameNode(template.Node):
    def __init__(self, titles):
        if len(titles) % 2:
            titles.append(None)
        self.crumbs = list(zip(titles[::2], titles[1::2]))

    def render(self, context):
        return '<ol class="breadcrumb">%s%s</ol>' % (
            ''.join(['<li><a href="%s">%s</a></li>' % (
                reverse(crumb[1].resolve(context)),
                crumb[0].resolve(context)
            ) for crumb in self.crumbs[:-1]]),
            '<li class="active">%s</li>' % self.crumbs[-1][0].resolve(context)
        )
