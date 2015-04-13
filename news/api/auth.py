from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from ..serializers import auth


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = auth.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = auth.GroupSerializer
