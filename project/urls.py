from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from access import api as access_api
from core import api as core_api


router = routers.DefaultRouter()
router.register(r'users', access_api.UserViewSet)
router.register(r'groups', access_api.GroupViewSet)
router.register(r'stories', core_api.StoryViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^', include(router.urls)) # main api
]
