# Generated by Django 4.0.4 on 2022-05-08 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0008_answers_users_assessments_alter_answers_users_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='number_assessments',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='users_assessments',
        ),
        migrations.RemoveField(
            model_name='answers',
            name='assessments',
        ),
        migrations.CreateModel(
            name='Assessments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessments', models.IntegerField(blank=True, verbose_name='Avaliações')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='assessments',
            field=models.ManyToManyField(blank=True, related_name='assessment', to='questions.assessments', verbose_name='Avaliações'),
        ),
    ]
