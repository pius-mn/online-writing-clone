# Generated by Django 4.0.2 on 2022-05-13 06:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_chatmessages'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
