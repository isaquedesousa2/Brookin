# Generated by Django 4.0.4 on 2022-05-08 17:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_answers_users_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='users_likes',
        ),
    ]
