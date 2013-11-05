from django.conf.urls import patterns, url
from prime.views import IssueView, ArticleView

urlpatterns = patterns('',
    url(r'^(?P<slug>[-_\w]+)?$', IssueView.as_view(), name='prime_issue'),
    url(r'^(?P<issue_slug>[-_\w]+)/(?P<article_slug>[-_\w]+)/$',
        ArticleView.as_view(), name='prime_article'),
)
