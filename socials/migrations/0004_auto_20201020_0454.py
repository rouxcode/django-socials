# Generated by Django 3.1.2 on 2020-10-20 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0003_auto_20201020_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramconfiguration',
            name='username',
            field=models.CharField(default='', max_length=64, verbose_name='Instagram Username'),
        ),
    ]