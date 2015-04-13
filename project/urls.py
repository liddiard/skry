from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = patterns('',

    # admin
    url(r'^admin/', include(admin.site.urls)),

    # other apps
    url(r'^prime/', include('prime.urls')),
    url(r'^research/', include('research.urls')),
    url(r'^music/', include('music.urls')),

    # news api
    url(r'^', include('news.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
