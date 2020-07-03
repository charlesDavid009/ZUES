# Generated by Django 2.2 on 2020-07-02 12:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_comments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='parent',
        ),
        migrations.AlterField(
            model_name='comment',
            name='comments',
            field=models.ManyToManyField(related_name='Commnets_count', to=settings.AUTH_USER_MODEL),
        ),
    ]