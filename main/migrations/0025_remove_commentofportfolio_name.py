# Generated by Django 4.0.1 on 2022-03-18 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_portfolios_commentofportfolio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentofportfolio',
            name='name',
        ),
    ]
