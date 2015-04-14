from rest_framework import viewsets

from . import serializers
from . import models


class StoryViewSet(viewsets.ModelViewSet):
    queryset = models.Story.objects.all()
    serializer_class = serializers.StorySerializer
    filter_fields = ('position',)
