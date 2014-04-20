from django.conf.urls import patterns, url
from blog.views import PostsView, PostView

urlpatterns = patterns('',
    url(r'^$', PostsView.as_view(), name='posts'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>\S+)/$', PostView.as_view(), name='post'),
)
