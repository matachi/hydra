from django.conf.urls import patterns, url
from blog.views import Posts

urlpatterns = patterns('',
    url(r'^$', Posts.as_view(), name='posts'),
)
