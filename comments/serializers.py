from rest_framework import serializers

from access import serializers as access_serializers
from . import models


class InternalCommentSerializer(serializers.HyperlinkedModelSerializer):
    user = access_serializers.UserSerializer()

    class Meta:
        model = models.InternalComment
        fields = "__all__"