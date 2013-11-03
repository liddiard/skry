from django.conf.urls import patterns, url
from prime.views import Front

urlpatterns = patterns('',
    url(r'^$', Front.as_view(), name='prime_front'),
)
