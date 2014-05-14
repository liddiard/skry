from django.conf.urls import patterns, url
from .views import MainView

urlpatterns = patterns('',
    url(r'^$', MainView.as_view(), name='main_page')
)

