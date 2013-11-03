from django.conf.urls import patterns, url
from prime.views import Front, Article

urlpatterns = patterns('',
    url(r'^$', Front.as_view(), name='prime_front'),
    url(r'^(?P<slug>[-_\w]+)/$', Article.as_view(), name='prime_article'),
)
