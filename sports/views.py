import django_filters
from rest_framework import viewsets, permissions

from . import serializers
from . import models


class SportViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Sport.objects.all()
    serializer_class = serializers.SportSerializer
    filter_fields = ()
    search_fields = ('name',)
    ordering_fields = "__all__"


class SchoolViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.School.objects.all()
    serializer_class = serializers.SchoolSerializer
    filter_fields = ()
    search_fields = ('name',)
    ordering_fields = "__all__"


class GameFilter(django_filters.FilterSet):
    class Meta:
        model = models.Game
        fields = {'sport': ['exact'],
                  'home_team': ['exact'],
                  'opposing_team': ['exact'],
                  'date': ['exact', 'gt', 'lt'],
                  'home_score': ['exact', 'gt', 'lt'],
                  'opposing_score': ['exact', 'gt', 'lt'],
                 }


class GameViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    filter_class = GameFilter
    search_fields = ()
    ordering_fields = "__all__"
