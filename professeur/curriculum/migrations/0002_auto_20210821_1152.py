# Generated by Django 3.2.5 on 2021-08-21 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='biography',
            options={'verbose_name': 'Biography', 'verbose_name_plural': 'Biographies'},
        ),
        migrations.AlterModelOptions(
            name='research',
            options={'verbose_name': 'Research', 'verbose_name_plural': 'Researches'},
        ),
    ]
