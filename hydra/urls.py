from django.conf.urls import patterns, include, url

from django.contrib import admin
from hydra.views import Main, Contact

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', Main.as_view(), name='index'),
    url(r'^contact/$', Contact.as_view(), name='contact'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
)
