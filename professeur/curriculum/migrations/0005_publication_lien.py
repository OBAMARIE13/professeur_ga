# Generated by Django 3.2.5 on 2021-08-27 05:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0004_auto_20210827_0502'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='lien',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
