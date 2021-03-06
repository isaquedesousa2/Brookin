# Generated by Django 4.0.4 on 2022-05-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_alter_questions_answers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='answer_user',
            field=models.CharField(max_length=10000, null=True, verbose_name='Resposta'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='assessments',
            field=models.IntegerField(blank=True, null=True, verbose_name='Avaliações'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='likes',
            field=models.IntegerField(blank=True, null=True, verbose_name='Curtidas'),
        ),
        migrations.AlterField(
            model_name='answers',
            name='number_assessments',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número de avaliações'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='answers',
            field=models.ManyToManyField(blank=True, related_name='answer', to='questions.answers', verbose_name='Respostas'),
        ),
    ]
