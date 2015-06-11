import json

from rest_framework import serializers
from reversion import models


class RevisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Revision


class VersionSerializer(serializers.ModelSerializer):
    revision = RevisionSerializer()
    serialized_data = serializers.SerializerMethodField()

    class Meta:
        model = models.Version

    def get_serialized_data(self, obj):
        # TODO: This is inefficent. We de-serialize the data and then the
        # Django Rest Framework serializer re-seraializes it. It really
        # shouldn't get serialized because it's already stored in a
        # serialized format, but I'm not sure if DRF provides a way to exempt
        # a field from serialization.
        return json.loads(obj.serialized_data)
