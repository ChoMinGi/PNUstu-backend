from django.conf import settings
from django.db import transaction
from django.utils import timezone
from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST
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
from .models import Announce
from .serializers import AnnounceListSerializer, AnnounceDetailSerializer
from medias.serializers import PhotoSerializer


class Announces(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_announces = Announce.objects.all()
        serializer = AnnounceListSerializer(
            all_announces,
            many=True,
            # KeyError get_is_owner(RoomListSerializer)의 request 키를 context로 import
            context={"request": request},
        )
        return Response(serializer.data)


class AnnounceDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Announce.objects.get(pk=pk)
        except Announce.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        announce = self.get_object(pk)
        serializer = serializers.AnnounceDetailSerializer(
            announce,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        announce = self.get_object(pk)
        if announce.owner != request.user:
            raise PermissionDenied
        # your magic

    def delete(self, request, pk):
        announce = self.get_object(pk)
        if announce.owner != request.user:
            raise PermissionDenied
        announce.delete()
        return Response(status=HTTP_204_NO_CONTENT)
