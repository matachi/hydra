from django.conf.urls import patterns, url
from projects.views import ProjectsView

urlpatterns = patterns('',
    url(r'^$', ProjectsView.as_view(), name='list'),
)
