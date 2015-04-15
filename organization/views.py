from rest_framework import viewsets

from . import serializers
from . import models


class SectionViewSet(viewsets.ModelViewSet):
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer
    filter_fields = ('parent', 'sites')
    search_fields = ('name', 'description', 'twitter', 'facebook')
    ordering_fields = "__all__"


class TagViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    filter_fields = ('series', 'sites')
    search_fields = ('name', 'description')
    ordering_fields = "__all__"
