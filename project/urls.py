from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

import news.views

from rest_framework import routers
from news import api

router = routers.DefaultRouter()
router.register(r'users', api.UserViewSet)
router.register(r'groups', api.GroupViewSet)

urlpatterns = patterns('',

    # admin
    url(r'^admin/', include(admin.site.urls)),

    # Django Rest Framework
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # other apps
    url(r'^prime/', include('prime.urls')),
    url(r'^research/', include('research.urls')),
    url(r'^music/', include('music.urls'))

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
