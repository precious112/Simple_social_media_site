# Generated by Django 3.2 on 2021-04-28 07:27

from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_alter_posts_date_of_release'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date_of_release',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
