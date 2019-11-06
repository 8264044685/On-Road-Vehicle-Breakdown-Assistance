# Generated by Django 2.2.4 on 2019-10-06 08:30

import datetime
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
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Car_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_no', models.TextField(max_length=50)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=255)),
                ('city_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('mobile_No', models.CharField(blank=True, max_length=25)),
                ('postal_code', models.CharField(blank=True, max_length=255)),
                ('profile_picture', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d')),
                ('user_type', models.CharField(choices=[('as_a', 'AS A'), ('mechanics', 'MECHANIC'), ('user', 'USER')], default='as_a', max_length=15)),
                ('car', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Car')),
                ('model_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Car_model')),
                ('services', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Services')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='mechanic_work_address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('services_name', models.TextField(blank=True)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('dist', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('pincode', models.IntegerField(blank=True)),
                ('address', models.TextField(max_length=300)),
                ('lat', models.FloatField(blank=True)),
                ('lang', models.FloatField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('userProfile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userProfile')),
            ],
        ),
        migrations.CreateModel(
            name='Districts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dist_name', models.CharField(max_length=50)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.State')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=50)),
                ('dist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.Districts')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.State')),
            ],
        ),
        
    ]