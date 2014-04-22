from django.conf.urls import patterns, include, url

from django.contrib import admin
from hydra.views import WelcomeView, AboutView, ContactView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', WelcomeView.as_view(), name='index'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^online-presence/$', ContactView.as_view(), name='contact'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
)
