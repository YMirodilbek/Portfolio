# Generated by Django 4.0.1 on 2022-03-20 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_commentofportfolio_portfolios_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentofportfolio',
            name='date',
        ),
        migrations.RemoveField(
            model_name='commentofportfolio',
            name='portfolio',
        ),
        migrations.RemoveField(
            model_name='commentofportfolio',
            name='portfolios',
        ),
    ]
