from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from access import views as access_views
from core import views as core_views


router = routers.DefaultRouter()

# access
router.register(r'users', access_views.UserViewSet)
router.register(r'groups', access_views.GroupViewSet)

# core
router.register(r'authors', core_views.AuthorViewSet)
router.register(r'statuses', core_views.StatusViewSet)
router.register(r'stories', core_views.StoryViewSet)
router.register(r'pages', core_views.PageViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^v1/', include(router.urls, namespace='v1')) # main api
]
