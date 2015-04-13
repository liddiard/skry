from rest_framework import viewsets

from ..serializers import core as serializers
from ..models import core as models


class StoryViewSet(viewsets.ModelViewSet):
    queryset = models.Story.objects.all()
    serializer_class = serializers.StorySerializer
    filter_fields = ('position',)
