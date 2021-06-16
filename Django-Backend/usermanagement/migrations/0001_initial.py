# Generated by Django 3.0.7 on 2020-06-10 20:16

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
            name='Waypoints',
            fields=[
                ('waypoint_id', models.AutoField(primary_key=True, serialize=False)),
                ('waypoint_name', models.CharField(max_length=255)),
                ('waypoint_description', models.TextField()),
                ('waypoint_logo', models.CharField(max_length=255)),
                ('waypoint_address', models.TextField()),
                ('waypoint_coords_lat', models.CharField(max_length=24)),
                ('waypoint_coords_lng', models.CharField(max_length=24)),
                ('waypoint_added', models.DateTimeField()),
                ('waypoint_url', models.CharField(max_length=255)),
                ('waypoint_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'waypoints',
            },
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ul_location_lat', models.FloatField()),
                ('ul_location_lng', models.FloatField()),
                ('ul_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
