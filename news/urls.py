from django.conf.urls import url
from rest_framework import routers

from news import api


router = routers.DefaultRouter()
router.register(r'users', api.auth.UserViewSet)
router.register(r'groups', api.auth.GroupViewSet)
router.register(r'stories', api.core.StoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
