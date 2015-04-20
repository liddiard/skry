from rest_framework import viewsets, permissions

from . import serializers
from . import models


class CardSizeViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.CardSize.objects.all()
    serializer_class = serializers.CardSizeSerializer
    filter_fields = ('width', 'height')
    search_fields = ()
    ordering_fields = "__all__"


class StylesheetViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Stylesheet.objects.all()
    serializer_class = serializers.StylesheetSerializer
    filter_fields = ()
    search_fields = ('name', 'file')
    ordering_fields = "__all__"


class ScriptViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Script.objects.all()
    serializer_class = serializers.ScriptSerializer
    filter_fields = ()
    search_fields = ('name', 'file')
    ordering_fields = "__all__"


class TemplateViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Template.objects.all()
    serializer_class = serializers.TemplateSerializer
    filter_fields = ('stylesheets', 'scripts')
    search_fields = ('name', 'file')
    ordering_fields = "__all__"
