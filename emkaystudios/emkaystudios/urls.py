from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Site
    # url(r'^blog/', 'emkaystudios.views.blog'),
    # url(r'^about/$', 'emkaystudios.views.about'),
    # url(r'^contact/$', 'emkaystudios.views.contact'),
    # url(r'^portfolio/$', 'emkaystudios.views.portfolio'),
    # url(r'^subscribe/$', 'emkaystudios.views.subscribe'),
    url(r'^$', include('home.urls')),
)

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
