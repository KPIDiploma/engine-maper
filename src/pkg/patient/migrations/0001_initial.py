# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-06 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Last name')),
                ('fullname', models.CharField(max_length=300, verbose_name='Full name')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='date of the birth')),
                ('address', models.CharField(blank=True, max_length=300, null=True, verbose_name='Address')),
                ('mobile', models.CharField(blank=True, max_length=13, null=True, verbose_name='Mobile number')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='E-mail')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='username')),
                ('sex', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=6, null=True)),
                ('blood_type', models.CharField(blank=True, choices=[('0+', 'First_positive'), ('0-', 'First_negative'), ('A+', 'Second_positive'), ('A-', 'Second_negative'), ('B+', 'Third_positive'), ('B-', 'Third_negative'), ('AB+', 'Fourth_positive'), ('AB-', 'Fourth_negative')], max_length=3, null=True)),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Live'), (1, 'Hospital'), (2, 'Dead')], null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=300, verbose_name='Full name')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='doctors',
            field=models.ManyToManyField(to='patient.Doctor'),
        ),
        migrations.AddField(
            model_name='patient',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='patient',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
