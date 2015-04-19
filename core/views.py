import django_filters
from rest_framework import viewsets

from . import serializers
from . import models


class StatusViewSet(viewsets.ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    filter_fields = ()
    search_fields = ('name',)
    ordering_fields = "__all__"


class StoryFilter(django_filters.FilterSet):
    published_at_or_after = django_filters.NumberFilter(name='publish_time',
                                                        lookup_type='gte')
    published_at_or_before = django_filters.NumberFilter(name='publish_time',
                                                         lookup_type='lte')

    class Meta:
        model = models.Story
        fields = ['status', 'authors', 'position', 'sections', 'tags', 'sites',
                  'publish_time', 'published_at_or_after',
                  'published_at_or_before']


class StoryViewSet(viewsets.ModelViewSet):
    queryset = models.Story.objects.all()
    serializer_class = serializers.StorySerializer
    filter_class = StoryFilter
    search_fields = ('title', 'teaser', 'subhead', 'body')
    ordering_fields = "__all__"


class PageViewSet(viewsets.ModelViewSet):
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
    filter_fields = ('parent', 'site')
    search_fields = ('title', 'body')
    ordering_fields = "__all__"
