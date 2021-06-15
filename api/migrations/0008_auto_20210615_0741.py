# Generated by Django 3.2.4 on 2021-06-15 07:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210615_0733'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meetups',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='meetups',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
