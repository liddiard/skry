import django_filters
from rest_framework import viewsets

from revisions.views import VersionableModelViewSetMixin
from . import serializers
from . import models


class PhotoRequestFilter(django_filters.FilterSet):
    class Meta:
        model = models.PhotoRequest
        fields = {'story': ['exact'],
                  'assignees': ['exact'],
                  'time': ['exact', 'lt', 'gt']
                 }


class PhotoRequestViewSet(VersionableModelViewSetMixin, viewsets.ModelViewSet):
    queryset = models.PhotoRequest.objects.all()
    serializer_class = serializers.PhotoRequestSerializer
    filter_class = PhotoRequestFilter
    search_fields = ('instructions', 'location', 'subject_info')
    ordering_fields = "__all__"


class GraphicRequestViewSet(VersionableModelViewSetMixin,
                            viewsets.ModelViewSet):
    queryset = models.GraphicRequest.objects.all()
    serializer_class = serializers.GraphicRequestSerializer
    filter_fields = ('story', 'assignees')
    search_fields = ('instructions', 'external_link')
    ordering_fields = "__all__"


class IllustrationRequestViewSet(VersionableModelViewSetMixin,
                                 viewsets.ModelViewSet):
    queryset = models.GraphicRequest.objects.all()
    serializer_class = serializers.GraphicRequestSerializer
    filter_fields = ('story', 'assignees')
    search_fields = ('instructions', 'external_link')
    ordering_fields = "__all__"
