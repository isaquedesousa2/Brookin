# Generated by Django 4.0.4 on 2022-05-17 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0033_alter_answers_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='level',
            field=models.CharField(choices=[('Ensino fundamental (básico)', 'Ensino fundamental (básico)'), ('Ensino médio (secundário)', 'Ensino médio (secundário)'), ('Ensino superior', 'Ensino superior')], max_length=50),
        ),
    ]
