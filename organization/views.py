from django.contrib.sites.models import Site
from rest_framework import viewsets, permissions

from . import serializers
from . import models


class SectionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Section.objects.all()
    serializer_class = serializers.SectionSerializer
    filter_fields = ('parent', 'sites')
    search_fields = ('name', 'description', 'twitter', 'facebook')
    ordering_fields = "__all__"


class TagViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagSerializer
    filter_fields = ('series', 'sites')
    search_fields = ('name', 'description')
    ordering_fields = "__all__"


class SiteViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = Site.objects.all()
    serializer_class = serializers.SiteSerializer
    filter_fields = ()
    search_fields = ('domain', 'name')
    ordering_fields = "__all__"
