# Generated by Django 3.1.2 on 2021-03-14 21:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default=None, max_length=50)),
                ('city', models.CharField(default=None, max_length=50)),
                ('area', models.CharField(default=None, max_length=50)),
                ('road', models.CharField(default=None, max_length=50)),
                ('contact', models.CharField(default=None, max_length=50)),
                ('location_coords', models.CharField(default=None, max_length=50)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
