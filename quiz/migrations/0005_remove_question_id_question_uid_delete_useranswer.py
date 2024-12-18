# Generated by Django 4.2.17 on 2024-12-17 16:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("quiz", "0004_useranswer"),
    ]

    operations = [
        migrations.RemoveField(model_name="question", name="id",),
        migrations.AddField(
            model_name="question",
            name="uid",
            field=models.UUIDField(
                default=uuid.uuid4, primary_key=True, serialize=False
            ),
        ),
        migrations.DeleteModel(name="UserAnswer",),
    ]
