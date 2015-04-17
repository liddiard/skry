from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from access import views as access_views
from attachments import views as attachments_views
from comments import views as comments_views
from core import views as core_views
from organization import views as organization_views
from requests import views as requests_views


router = routers.DefaultRouter()

# access
router.register(r'users', access_views.UserViewSet)
router.register(r'groups', access_views.GroupViewSet)

# attachments
router.register(r'images', attachments_views.ImageViewSet)
router.register(r'videos', attachments_views.VideoViewSet)
router.register(r'audio', attachments_views.AudioViewSet)
router.register(r'polls', attachments_views.PollViewSet)
router.register(r'poll_choices', attachments_views.PollChoiceViewSet)

# comments
router.register(r'internal_comments', comments_views.InternalCommentViewSet)

# core
router.register(r'authors', core_views.AuthorViewSet)
router.register(r'statuses', core_views.StatusViewSet)
router.register(r'stories', core_views.StoryViewSet)
router.register(r'pages', core_views.PageViewSet)

# organization
router.register(r'sections', organization_views.SectionViewSet)
router.register(r'tags', organization_views.TagViewSet)

# requests
router.register(r'photo_requests', requests_views.PhotoRequestViewSet)
router.register(r'graphic_requests', requests_views.GraphicRequestViewSet)
router.register(r'illustration_requests',
                requests_views.IllustrationRequestViewSet)


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/token/', include('rest_auth.urls')),
    url(r'^auth/web/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^v1/', include(router.urls, namespace='v1')) # main api
]
