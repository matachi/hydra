from django.conf.urls import patterns, include, url

from django.contrib import admin
from hydra.views import Main

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hydra.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', Main.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
