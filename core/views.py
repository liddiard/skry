import json

import django_filters
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from revisions.views import VersionableModelViewSetMixin
from . import serializers
from . import models


class SchemaViewSet(viewsets.ViewSet):
    """Returns a JSON document representing the entire project's apps, models,
    and model fields and the requesting user's permissions to perform actions
    on models.
    """

    permission_classes = (permissions.IsAuthenticated,)

    @method_decorator(cache_page(60*60)) # cache view for one hour
    def list(self, request):
        return Response(serializers.schema_serializer(request))


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


class StoryViewSet(VersionableModelViewSetMixin, viewsets.ModelViewSet):
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
                                             publish_time__lte=timezone.now())


class PageViewSet(VersionableModelViewSetMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Page.objects.all()
    serializer_class = serializers.PageSerializer
    filter_fields = ('parent', 'site')
    search_fields = ('title', 'body')
    ordering_fields = "__all__"
