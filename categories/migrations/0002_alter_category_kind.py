# Generated by Django 4.1.3 on 2022-11-27 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="kind",
            field=models.CharField(
                blank=True,
                choices=[
                    ("announces", "공지사항"),
                    ("benefits", "제휴혜택"),
                    ("inquiries", "문의/건의"),
                    ("petitions", "청원 게시판"),
                    ("serveys", "설문조사"),
                ],
                max_length=15,
                null=True,
            ),
        ),
    ]
