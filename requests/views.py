from rest_framework import viewsets

from . import serializers
from . import models


class PhotoRequestViewSet(viewsets.ModelViewSet):
    queryset = models.PhotoRequest.objects.all()
    serializer_class = serializers.PhotoRequestSerializer
    filter_fields = ('story', 'assignees', 'time')
    search_fields = ('instructions', 'location', 'subject_info')
    ordering_fields = "__all__"


class GraphicRequestViewSet(viewsets.ModelViewSet):
    queryset = models.GraphicRequest.objects.all()
    serializer_class = serializers.GraphicRequestSerializer
    filter_fields = ('story', 'assignees')
    search_fields = ('instructions', 'external_link')
    ordering_fields = "__all__"


class IllustrationRequestViewSet(viewsets.ModelViewSet):
    queryset = models.GraphicRequest.objects.all()
    serializer_class = serializers.GraphicRequestSerializer
    filter_fields = ('story', 'assignees')
    search_fields = ('instructions', 'external_link')
    ordering_fields = "__all__"
