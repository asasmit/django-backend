# Generated by Django 4.0.6 on 2024-12-16 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_useranswer'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserAnswer',
        ),
    ]
