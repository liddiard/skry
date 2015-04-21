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
    date_on_or_after = django_filters.NumberFilter(name='date',
                                                   lookup_type='gte')
    date_on_or_before = django_filters.NumberFilter(name='date',
                                                    lookup_type='lte')
    home_score_greater_than_or_equal_to = django_filters.\
                                               NumberFilter(name='home_score',
                                                            lookup_type='gte')
    opposing_score_greater_than_or_equal_to = django_filters.\
                                           NumberFilter(name='opposing_score',
                                                        lookup_type='gte')
    home_score_less_than_or_equal_to = django_filters.\
                                               NumberFilter(name='home_score',
                                                            lookup_type='lte')
    opposing_score_less_than_or_equal_to = django_filters.\
                                           NumberFilter(name='opposing_score',
                                                        lookup_type='lte')

    class Meta:
        model = models.Game
        fields = ['sport', 'home', 'opposing', 'date', 'date_on_or_after',
                  'date_on_or_before', 'home_score_greater_than_or_equal_to',
                  'opposing_score_greater_than_or_equal_to',
                  'home_score_less_than_or_equal_to',
                  'opposing_score_less_than_or_equal_to']


class GameViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Game.objects.all()
    serializer_class = serializers.GameSerializer
    filter_class = GameFilter
    search_fields = ()
    ordering_fields = "__all__"
