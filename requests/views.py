import django_filters
from rest_framework import viewsets

from revisions.views import VersionableModelViewSetMixin
from . import serializers
from . import models


class PhotoRequestFilter(django_filters.FilterSet):
    time_at_or_after = django_filters.NumberFilter(name='time',
                                                   lookup_type='gte')
    time_at_or_before = django_filters.NumberFilter(name='time',
                                                    lookup_type='lte')

    class Meta:
        model = models.PhotoRequest
        fields = ['story', 'assignees', 'time', 'time_at_or_after',
                  'time_at_or_before']


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
