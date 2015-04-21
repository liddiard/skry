from django.utils.timezone import now
import django_filters
from rest_framework import viewsets, permissions

from . import serializers
from . import models


class StatusViewSet(viewsets.ModelViewSet):
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer
    filter_fields = ()
    search_fields = ('name',)
    ordering_fields = "__all__"


class StoryFilter(django_filters.FilterSet):
    publish_at_or_after = django_filters.NumberFilter(name='publish_time',
                                                      lookup_type='gte')
    publish_at_or_before = django_filters.NumberFilter(name='publish_time',
                                                       lookup_type='lte')

    class Meta:
        model = models.Story
        fields = ['status', 'authors', 'position', 'sections', 'tags', 'sites',
                  'publish_time', 'publish_at_or_after',
                  'publish_at_or_before']


class StoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Story.objects.all()
    serializer_class = serializers.StorySerializer
    filter_class = StoryFilter
    search_fields = ('title', 'teaser', 'subhead', 'body')
    ordering_fields = "__all__"

    def get_queryset(self):
        if self.request.user.is_authenticated():
            return models.Story.objects.all()
        else:
            # restrict viewable stories to those which are published
            final_status = models.Status.objects.last()
            return models.Story.objects.filter(status=final_status,
                                               publish_time__lte=now())


class PageViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
    filter_fields = ('parent', 'site')
    search_fields = ('title', 'body')
    ordering_fields = "__all__"
