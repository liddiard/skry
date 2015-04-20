from rest_framework import viewsets, permissions

from . import serializers
from . import models


class AuthorViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)
    queryset = models.Author.objects.all()
    filter_fields = ()
    search_fields = ('first_name', 'last_name', 'organization', 'title',
                     'email', 'twitter', 'bio')
    ordering_fields = "__all__"

    def get_serializer_class(self):
        if self.request.user.is_authenticated():
            return serializers.AuthenticatedAuthorSerializer
        else:
            return serializers.AuthorSerializer
