# Generated by Django 3.2.7 on 2021-11-07 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0002_alter_user_email'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Account',
        ),
    ]
