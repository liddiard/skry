from rest_framework import viewsets

from . import serializers
from . import models


class InternalCommentViewSet(viewsets.ModelViewSet):
    queryset = models.InternalComment.objects.all()
    serializer_class = serializers.InternalCommentSerializer
    filter_fields = ('user', 'time_posted', 'content_type', 'object_id')
    search_fields = ('text',)
    ordering_fields = "__all__"
