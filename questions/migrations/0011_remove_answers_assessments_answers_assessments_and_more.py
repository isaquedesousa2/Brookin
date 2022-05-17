# Generated by Django 4.0.4 on 2022-05-08 19:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0010_answers_number_assessments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='assessments',
        ),
        migrations.AddField(
            model_name='answers',
            name='assessments',
            field=models.IntegerField(blank=True, default=1, verbose_name='Avaliações'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answers',
            name='number_assessments',
            field=models.IntegerField(blank=True, verbose_name='Número de avaliações'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='users_likes',
            field=models.ManyToManyField(blank=True, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='Usuário que curtiram'),
        ),
        migrations.DeleteModel(
            name='Assessments',
        ),
    ]