# Generated by Django 4.0.3 on 2022-04-08 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_rename_delivery_jobs_delivery_qty_jobs_delivery_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='messages',
            name='chat',
        ),
        migrations.DeleteModel(
            name='Chats',
        ),
        migrations.DeleteModel(
            name='Messages',
        ),
    ]
