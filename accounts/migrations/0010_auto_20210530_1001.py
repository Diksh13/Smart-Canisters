# Generated by Django 3.1.7 on 2021-05-30 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_login_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='last_login',
            field=models.DateTimeField(null=True),
        ),
        migrations.DeleteModel(
            name='Login_Details',
        ),
    ]
