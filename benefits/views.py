from django.conf import settings
from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import (
    NotAuthenticated,
    NotFound,
    ParseError,
    PermissionDenied,
)
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from categories.models import Category
from .models import Benefit
from .serializers import BenefitListSerializer
from medias.serializers import PhotoSerializer


class Benefits(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_benefits = Benefit.objects.all()
        serializer = BenefitListSerializer(
            all_benefits,
            many=True,
            # KeyError get_is_owner(RoomListSerializer)의 request 키를 context로 import
            context={"request": request},
        )
        return Response(serializer.data)
