# Generated by Django 3.1.2 on 2020-10-21 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0012_auto_20201021_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instagramconfiguration',
            name='username',
            field=models.CharField(default='', help_text='get posts of one user is possible. no hashtags, no special things. username is only for visual help - the only relevant thing is the token', max_length=64, verbose_name='Instagram Username'),
        ),
    ]
