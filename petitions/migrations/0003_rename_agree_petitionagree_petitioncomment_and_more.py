# Generated by Django 4.1.3 on 2022-11-29 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("comments", "0003_remove_comment_petitions_alter_comment_payload"),
        ("petitions", "0002_petition_agree"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Agree",
            new_name="PetitionAgree",
        ),
        migrations.CreateModel(
            name="PetitionComment",
            fields=[
                (
                    "comment_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="comments.comment",
                    ),
                ),
                (
                    "petition",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="comments",
                        to="petitions.petition",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=("comments.comment",),
        ),
        migrations.AddField(
            model_name="petition",
            name="comment",
            field=models.ManyToManyField(
                related_name="petition_comment", to="petitions.petitioncomment"
            ),
        ),
    ]
