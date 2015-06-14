import django_filters
from rest_framework import viewsets

from revisions.views import VersionableModelViewSetMixin
from . import serializers
from . import models


class InternalCommentFilter(django_filters.FilterSet):
    class Meta:
        model = models.InternalComment
        fields = {'user': ['exact'],
                  'time_posted': ['exact', 'lt', 'gt'],
                  'content_type': ['exact'],
                  'object_id': ['exact']
                 }


class InternalCommentViewSet(VersionableModelViewSetMixin,
                             viewsets.ModelViewSet):
    queryset = models.InternalComment.objects.all()
    serializer_class = serializers.InternalCommentSerializer
    filter_class = InternalCommentFilter
    search_fields = ('text',)
    ordering_fields = "__all__"
