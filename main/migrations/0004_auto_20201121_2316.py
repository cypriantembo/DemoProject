# Generated by Django 3.1.2 on 2020-11-21 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201114_1859'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Demo',
        ),
        migrations.RemoveField(
            model_name='client',
            name='cell',
        ),
        migrations.RemoveField(
            model_name='client',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='client',
            name='location',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='cell',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='driver',
            name='location',
        ),
        migrations.AddField(
            model_name='client',
            name='area',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='city',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='contact',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='location_coords',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='client',
            name='road',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='driver',
            name='area',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='driver',
            name='city',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='driver',
            name='company',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='driver',
            name='contact',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='driver',
            name='location_coords',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='driver',
            name='road',
            field=models.CharField(default=None, max_length=50),
        ),
    ]