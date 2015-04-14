from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_fields = ('groups', 'user_permissions', 'is_staff', 'is_active',
                     'is_superuser')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering_fields = ('username', 'first_name', 'last_name', 'email',
                       'last_login', 'date_joined')


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    filter_fields = ('permissions',)
    search_fields = ('name',)
    ordering_fields = ('name',)
