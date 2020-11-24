# Generated by Django 3.1.2 on 2020-11-14 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('cell', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Demo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='driver',
            name='email',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='num_stars',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='transaction_name',
        ),
        migrations.AddField(
            model_name='transactions',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='stars',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='transactions',
            name='transaction_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='transactions',
            name='waste_type',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='amount',
            field=models.DecimalField(decimal_places=0, max_digits=4),
        ),
        migrations.AlterField(
            model_name='transactions',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
