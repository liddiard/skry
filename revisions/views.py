from rest_framework import viewsets, permissions
from reversion import models

from . import serializers


class VersionViewSet(viewsets.ModelViewSet):
    queryset = models.Version.objects.all()
    serializer_class = serializers.VersionSerializer
    # filter_fields = ('content_type', 'object_id', 'revision__user',
    #                  'revision__data_created')
    # search_fields = ('serialized_data', 'revision__comment')
    ordering_fields = "__all__"
