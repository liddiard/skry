from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Permission


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    permissions = PermissionSerializer(many=True)

    class Meta:
        model = Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User
        exclude = ('password',)
