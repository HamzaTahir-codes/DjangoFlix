# Generated by Django 5.1.7 on 2025-03-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_video_timestamp_video_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_id',
            field=models.CharField(max_length=220, unique=True),
        ),
    ]
