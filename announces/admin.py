from django.contrib import admin
from .models import Announce


@admin.action(description="Set all prices to zero")
# 3개의 변수를 받는다 (이 액션을 가지는 모델 관리자, 액션 요청하는 user 정보, 직접 선택한 요소)
def reset_prices(model_admin, request, rooms):
    for room in rooms.all():
        room.price = 0
        room.save()

    print(dir(request.user))

    pass


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    # Always import actions in the ADMIN
    actions = (reset_prices,)

    list_display = (
        "name",
        "price",
        "kind",
        "total_amenities",
        "rating",
        "owner",
        "created_at",
    )
    search_fields = (
        #
        "owner__username",
    )
    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
        "created_at",
        "updated_at",
    )


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
