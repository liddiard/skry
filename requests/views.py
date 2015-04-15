from rest_framework import viewsets

from . import serializers
from . import models


class PhotoRequestViewSet(viewsets.ModelViewSet):
    queryset = models.PhotoRequest.objects.all()
    serializer_class = serializers.PhotoRequestSerializer
    filter_fields = ('story', 'assignees',) # TODO: pick up here
    search_fields = ('first_name', 'last_name', 'organization', 'title',
                     'email', 'twitter', 'bio')
    ordering_fields = "__all__"
