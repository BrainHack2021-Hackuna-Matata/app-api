# Generated by Django 3.2.4 on 2021-06-16 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210616_1114'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='imageurl',
            new_name='name',
        ),
    ]
