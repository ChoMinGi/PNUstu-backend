from rest_framework import serializers
from .models import Survey
from users.serializers import SimpleUserSerializer
from comments.serializers import CommentSerializer
from categories.serializers import CategorySerializer

class SurveyMainListSerializer(serializers.ModelSerializer):
    total_submission = serializers.SerializerMethodField()
    