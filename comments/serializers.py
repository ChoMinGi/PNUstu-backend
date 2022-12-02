from rest_framework import serializers
from users.serializers import SimpleUserSerializer
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = (
            "user",
             "payload",
             )
