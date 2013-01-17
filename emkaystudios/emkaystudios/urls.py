from django.conf.urls import patterns, include, url

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
    # url(r'^$', 'emkaystudios.views.index'),
)
