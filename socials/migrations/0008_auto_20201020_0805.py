# Generated by Django 3.1.2 on 2020-10-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socials', '0007_auto_20201020_0756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-date'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='original_id',
            field=models.CharField(default='dddd', max_length=128, verbose_name='Original ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True, verbose_name='published/visible'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(verbose_name='Post Date'),
        ),
        migrations.AlterUniqueTogether(
            name='post',
            unique_together={('configuration', 'original_id')},
        ),
        migrations.RemoveField(
            model_name='post',
            name='is_visible',
        ),
        migrations.RemoveField(
            model_name='post',
            name='originalid',
        ),
    ]