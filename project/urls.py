from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

import news.views

urlpatterns = patterns('',
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # admin
    url(r'^admin/', include(admin.site.urls)),

    # main site
    url(r'^$', news.views.CategoryView.as_view(), name='news_front'),
    url(r'^category/(?P<category>\S+)/$', news.views.CategoryView.as_view(), name='news_category'),
    url(r'^article/(?P<id>\S+)/$', news.views.ArticleView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<slug>\S+)/$', news.views.ArticleView.as_view(), name='news_article'),

    # api
    url(r'^api/article/position-change/$', news.views.ArticlePositionChangeView.as_view()),
    url(r'^api/article/get-cards/$', news.views.CardsJSONView.as_view()),

    # other apps
    url(r'^prime/', include('prime.urls')),
    url(r'^music/', include('music.urls'))
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
