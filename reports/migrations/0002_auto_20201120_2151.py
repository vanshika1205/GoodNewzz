# Generated by Django 3.0.6 on 2020-11-20 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloodpressure',
            name='diastole',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='bloodpressure',
            name='systole',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Sugar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=0)),
                ('time', models.DateTimeField(auto_now=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
