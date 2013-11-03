from django.conf.urls import patterns, include, url
from main.views import Front
from dailybruin.settings.base import MEDIA_URL, MEDIA_ROOT

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dailybruin.views.home', name='home'),
    # url(r'^dailybruin/', include('dailybruin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # front
    url(r'^$', Front.as_view(), name='front'),

    # admin
    url(r'^admin/', include(admin.site.urls)),

    # media
    (r'^%s(?P<path>.*)$' % MEDIA_URL[1:], 'django.views.static.serve', {
                 'document_root': MEDIA_ROOT}),

    # mainsite

    # other apps
    url(r'^prime/', include('prime.urls')),
)
