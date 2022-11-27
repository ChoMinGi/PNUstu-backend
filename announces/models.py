from django.db import models
from common.models import CommonModel


class Announce(CommonModel):
    class TopicKindChoices(models.TextChoices):
        JOB_EMPLOY = ("job_employ", "취업")
        WELFARE = ("stu_welfare", "복지")
        FACILITES = ("facilities", "시설")

    title = models.CharField(
        max_length=300,
        default="",
    )
    content = models.CharField(
        max_length=3000,
        default="",
    )
    writer = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="announces",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="announces",
    )

    is_important = models.BooleanField(
        default=False,
    )

    def __str__(self) -> str:
        return self.name
