from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from access import views as access_views
from attachments import views as attachments_views
from authors import views as authors_views
from comments import views as comments_views
from core import views as core_views
from display import views as display_views
from organization import views as organization_views
from requests import views as requests_views
from revisions import views as revisions_views
from sports import views as sports_views


router = routers.DefaultRouter()

# get the view for auto-generated API docs from Swagger
docs_view = get_swagger_view(title='docs')

# access
router.register(r'users', access_views.UserViewSet)
router.register(r'groups', access_views.GroupViewSet)
router.register(r'permissions', access_views.PermissionViewSet)

# attachments
router.register(r'images', attachments_views.ImageViewSet)
router.register(r'videos', attachments_views.VideoViewSet)
router.register(r'audio', attachments_views.AudioViewSet)
router.register(r'reviews', attachments_views.ReviewViewSet)
router.register(r'polls', attachments_views.PollViewSet)
router.register(r'poll_choices', attachments_views.PollChoiceViewSet)

# authors
router.register(r'authors', authors_views.AuthorViewSet)
router.register(r'organizations', authors_views.OrganizationViewSet)
router.register(r'positions', authors_views.PositionViewSet)

# comments
router.register(r'internal_comments', comments_views.InternalCommentViewSet)

# core
router.register(r'schema', core_views.SchemaViewSet, base_name='schema')
router.register(r'statuses', core_views.StatusViewSet)
router.register(r'stories', core_views.StoryViewSet)
router.register(r'pages', core_views.PageViewSet)

# display
router.register(r'card_sizes', display_views.CardSizeViewSet)
router.register(r'stylesheets', display_views.StylesheetViewSet)
router.register(r'scripts', display_views.ScriptViewSet)
router.register(r'templates', display_views.TemplateViewSet)

# organization
router.register(r'sections', organization_views.SectionViewSet)
router.register(r'tags', organization_views.TagViewSet)
router.register(r'sites', organization_views.SiteViewSet)

# requests
router.register(r'photo_requests', requests_views.PhotoRequestViewSet)
router.register(r'graphic_requests', requests_views.GraphicRequestViewSet)
router.register(r'illustration_requests',
                requests_views.IllustrationRequestViewSet)

# sports
router.register(r'sports', sports_views.SportViewSet)
router.register(r'schools', sports_views.SchoolViewSet)
router.register(r'games', sports_views.GameViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^auth/token/', include('rest_auth.urls')),
    url(r'^auth/web/', include('rest_framework.urls',
                               namespace='rest_framework')),
    url(r'^docs/', docs_view),
    url(r'^v1/', include(router.urls, namespace='v1')) # main api
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # serve user-uploaded media in development environment
