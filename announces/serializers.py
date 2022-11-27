from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Announce
from medias.serializers import PhotoSerializer
from users.serializers import SimpleUserSerializer


class AnnounceListSerializer(ModelSerializer):

    is_writer = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Announce
        field = (
            "pk",
            "title",
            "is_writer",
            "pk",
            "pk",
        )

    def get_is_writer(self, announce):
        # dynamic field 동적필드
        request = self.context["request"]
        return announce.owner == request.user
