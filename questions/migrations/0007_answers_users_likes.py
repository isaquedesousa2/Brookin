# Generated by Django 4.0.4 on 2022-05-08 17:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0006_remove_answers_users_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='users_likes',
            field=models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Usuário que curtiram'),
        ),
    ]