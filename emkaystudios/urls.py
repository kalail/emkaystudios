from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'emkaystudios.views.home', name='home'),
    # url(r'^emkaystudios/', include('emkaystudios.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^blog/', include(blog.urls)),
    url(r'^about/$', 'emkaystudios.views.about'),
    url(r'^contact/$', 'emkaystudios.views.contact'),
    url(r'^archive/$', 'emkaystudios.views.archive'),
    url(r'^coming-soon/$', 'emkaystudios.views.coming_soon'),
    url(r'^$', 'emkaystudios.views.index'),
)
