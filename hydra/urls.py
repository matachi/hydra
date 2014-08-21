from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from hydra.views import WelcomeView, AboutView, ContactView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', WelcomeView.as_view(), name='index'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^online-presence/$', ContactView.as_view(), name='contact'),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'^projects/', include('projects.urls', namespace='projects')),
    url(r'^comments/', include('django_comments_xtd.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns = urlpatterns + \
                  static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT) + \
                  static(settings.MEDIA_URL,
                         document_root=settings.MEDIA_ROOT)

