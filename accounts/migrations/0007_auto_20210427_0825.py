# Generated by Django 3.1.7 on 2021-04-27 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20210427_0823'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('r_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('r_name', models.CharField(max_length=30)),
                ('r_email', models.EmailField(max_length=30)),
                ('r_password', models.CharField(max_length=30)),
                ('r_role', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Registerr',
        ),
    ]