from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Announce
from users.serializers import SimpleUserSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer


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
            "is_important",
        )

    def get_is_writer(self, announce):
        # dynamic field 동적필드
        request = self.context["request"]
        return announce.owner == request.user


class AnnounceDetailSerializer(ModelSerializer):
    writer = SimpleUserSerializer(read_only=True)
    category = CategorySerializer(
        read_only=True,
    )
    is_writer = serializers.SerializerMethodField()
    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Announce
        fields = "__all__"

    def get_is_writer(self, room):
        # dynamic field 동적필드
        request = self.context["request"]
        return room.owner == request.user
