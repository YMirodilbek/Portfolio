# Generated by Django 4.0.1 on 2022-03-27 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_commentofportfolio_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
