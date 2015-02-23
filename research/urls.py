from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.FrontView.as_view(), name='research_front'),
    url(r'^posts/$', views.PostsView.as_view(), name='research_posts'),
    url(r'^projects/$', views.ProjectsView.as_view(),
        name='research_projects'),
    url(r'^post/(?P<slug>[-_\w]+)/$', views.PostView.as_view(),
        name='research_post'),
    url(r'^project/(?P<slug>[-_\w]+)/$', views.ProjectView.as_view(),
        name='research_project'),
)
