# Generated by Django 4.0.4 on 2022-05-05 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_answers_number_assessments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='number_assessments',
            field=models.IntegerField(blank=True, verbose_name='Número de avaliações'),
        ),
    ]