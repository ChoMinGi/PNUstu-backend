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
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from .models import Announce


class Announces(APIView):
    def get(self, request):
        all_announces = Announce.objects.all()
        serializer = AnnounceSerializer(all_announces, many=True)
        return Response(serializer.data)
