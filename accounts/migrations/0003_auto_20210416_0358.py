# Generated by Django 3.1.7 on 2021-04-16 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_login_l_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Login',
            new_name='Register',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='l_email',
            new_name='r_email',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='l_name',
            new_name='r_name',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='l_password',
            new_name='r_password',
        ),
        migrations.RenameField(
            model_name='register',
            old_name='l_role',
            new_name='r_role',
        ),
    ]
