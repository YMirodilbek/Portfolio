# Generated by Django 4.0.1 on 2022-03-18 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_alter_portfolios_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='portfolios',
            name='category',
        ),
    ]
