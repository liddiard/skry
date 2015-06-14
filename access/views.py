from django.contrib.auth.models import User, Group, Permission
from rest_framework import viewsets

from . import serializers


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {'groups': ['exact'],
                  'user_permissions': ['exact'],
                  'is_staff': ['exact'],
                  'is_active': ['exact'],
                  'is_superuser': ['exact'],
                  'last_login': ['exact', 'gt', 'lt'],
                  'date_joined': ['exact', 'gt', 'lt']
                 }


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    filter_class = UserFilter
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering_fields = ('username', 'first_name', 'last_name', 'email',
                       'last_login', 'date_joined', 'is_staff', 'is_active',
                       'is_superuser')


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    filter_fields = ('permissions',)
    search_fields = ('name',)
    ordering_fields = "__all__"


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    serializer_class = serializers.PermissionSerializer
    filter_fields = ('content_type',)
    search_fields = ('name', 'codename')
    ordering_fields = "__all__"
