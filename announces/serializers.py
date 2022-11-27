from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Announce
from users.serializers import SimpleUserSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer


class AnnounceListSerializer(ModelSerializer):

    photos = PhotoSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Announce
        fields = (
            "pk",
            "title",
            "photos",
            "writer",
            "is_important",
        )


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

    def get_is_writer(self, announce):
        # dynamic field 동적필드
        request = self.context["request"]
        return announce.writer == request.user
