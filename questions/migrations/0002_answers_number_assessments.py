# Generated by Django 4.0.4 on 2022-05-05 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='number_assessments',
            field=models.FloatField(blank=True, default=0, verbose_name='Número de avaliações'),
            preserve_default=False,
        ),
    ]
