# Generated by Django 3.1.7 on 2021-04-27 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20210427_0823'),
        ('accounts', '0005_auto_20210426_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registerr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r_name', models.CharField(max_length=30)),
                ('r_email', models.EmailField(max_length=30)),
                ('r_password', models.CharField(max_length=30)),
                ('r_role', models.CharField(max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='Login',
        ),
        migrations.DeleteModel(
            name='Register',
        ),
    ]
