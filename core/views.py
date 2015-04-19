from rest_framework import viewsets

from . import serializers
from . import models


class StatusViewSet(viewsets.ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    filter_fields = ()
    search_fields = ('name',)
    ordering_fields = "__all__"


class StoryViewSet(viewsets.ModelViewSet):
    queryset = models.Story.objects.all()
    serializer_class = serializers.StorySerializer
    filter_fields = ('status', 'authors', 'position', 'sections', 'tags',
                     'sites')
    search_fields = ('title', 'teaser', 'subhead', 'body')
    ordering_fields = "__all__"


class PageViewSet(viewsets.ModelViewSet):
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
    filter_fields = ('parent', 'site')
    search_fields = ('title', 'body')
    ordering_fields = "__all__"
