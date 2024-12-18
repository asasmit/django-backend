# Generated by Django 4.2.17 on 2024-12-18 04:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0006_rename_text_question_question_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "uid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=20)),
                ("email", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=25)),
                ("marks", models.IntegerField(default=0)),
            ],
            options={"abstract": False,},
        ),
    ]
