from django.conf.urls import url, include
from rest_framework import routers

from news.api import auth, core


router = routers.DefaultRouter()
router.register(r'users', auth.UserViewSet)
router.register(r'groups', auth.GroupViewSet)
router.register(r'stories', core.StoryViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework'))
]
