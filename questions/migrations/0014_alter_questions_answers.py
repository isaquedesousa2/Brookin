# Generated by Django 4.0.4 on 2022-05-08 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_alter_answers_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answers',
            field=models.ManyToManyField(blank=True, null=True, related_name='answer', to='questions.answers', verbose_name='Respostas'),
        ),
    ]
