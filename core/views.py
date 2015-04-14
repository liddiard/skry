from rest_framework import viewsets

from . import serializers
from . import models


class StoryViewSet(viewsets.ModelViewSet):
    queryset = models.Story.objects.all()
    serializer_class = serializers.StorySerializer
    filter_fields = ('status', 'author', 'position', 'sections', 'tags',
                     'sites')
    search_fields = ('title', 'teaser', 'subhead', 'body')
    ordering_fields = "__all__"
