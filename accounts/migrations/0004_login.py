# Generated by Django 3.1.7 on 2021-04-26 07:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210416_0358'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('login_time', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('logout_time', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]
