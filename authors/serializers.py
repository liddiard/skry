from rest_framework import serializers

from access import serializers as access_serializers
from . import models


class OrganizationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Organization


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Position


class JobSerializer(serializers.HyperlinkedModelSerializer):
    position = PositionSerializer()
    is_current = serializers.SerializerMethodField()

    def get_is_current(self, obj):
        return obj.is_current()

    class Meta:
        model = models.Job
        exclude = ('author', 'url')


class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    organization = OrganizationSerializer()
    positions = JobSerializer(source='job_set', many=True)

    class Meta:
        model = models.Author
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(AuthorSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request and request.user.is_authenticated():
            self.fields['user'] = access_serializers.UserSerializer()
