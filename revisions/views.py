# -*- coding: utf-8 -*-

from rest_framework import viewsets, permissions
from rest_framework.decorators import detail_route
from rest_framework.response import Response
import reversion
from reversion.models import Version
from django.shortcuts import get_object_or_404

from . import serializers


class VersionableModelViewSetMixin(viewsets.ModelViewSet):
    """Provides routes to versioned models for listing revisions and reverting
    to them.

    Include this mixin on ModelViewSets which have their revision history
    tracked with django-reversion. It provides two endpoints:

    1. "/revisions" (method: GET) - append to a detail view URL (e.g.
       "/v1/stories/24/revisions") to view a list of revisions associated with
       this object.
    2. "/revert" (method: PUT) - append to a detail view URL (e.g.
       "/v1/stories/24/revert") and provide payload data in the format
       "revision: <revision_id>", where revision_id is the id of the revision
       associated with this object to which you want to revert this object.
       On success, will return HTTP 200 and JSON string of the object's fields
       at the specified revision. If no revision id is provided or an invalid
       revision id is provided (revision doesn't exist or revision is not
       associated with this object), a 404 error will be returned.

       Associated Django Rest Framework implementation docs:
       http://www.django-rest-framework.org/api-guide/viewsets/#marking-extra-actions-for-routing
    """

    @detail_route(methods=['get'])
    def revisions(self, request, pk=None):
        object = self.get_object()
        versions = reversion.get_for_object(object)
        version_serializer = serializers.VersionSerializer(versions, many=True)
        return Response(version_serializer.data)

    @detail_route(methods=['put'])
    def revert(self, request, pk=None):
        object = self.get_object()
        version = get_object_or_404(Version, object_id=object.id,
                                    id=request.data.get('revision'))
        # http://django-reversion.readthedocs.org/en/release-1.8.1/api.html#reverting-to-previous-revisions
        version.revert()
        return Response(version.field_dict)
