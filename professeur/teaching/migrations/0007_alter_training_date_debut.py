# Generated by Django 3.2.5 on 2021-08-31 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teaching', '0006_auto_20210831_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='training',
            name='date_debut',
            field=models.DateField(verbose_name='Date de début'),
        ),
    ]
