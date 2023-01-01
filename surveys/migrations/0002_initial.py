# Generated by Django 4.1.3 on 2022-12-25 16:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("categories", "0001_initial"),
        ("surveys", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="surveyparticipate",
            name="participant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="survey_participate",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="survey",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="surveys",
                to="categories.category",
            ),
        ),
        migrations.AddField(
            model_name="survey",
            name="participate",
            field=models.ManyToManyField(
                related_name="surveys", to="surveys.surveyparticipate"
            ),
        ),
        migrations.AddField(
            model_name="survey",
            name="writer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="surveys",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]