from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dailybruin.views.home', name='home'),
    # url(r'^dailybruin/', include('dailybruin.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),


    # admin
    url(r'^admin/', include(admin.site.urls)),

    # mainsite

    # other apps
    url(r'^prime/', include('prime.urls')),
    url(r'^music/', include('music.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
