# Generated by Django 4.0.1 on 2022-03-20 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_commentofportfolio_date_commentofportfolio_portfolio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentofportfolio',
            old_name='portfolio',
            new_name='name',
        ),
    ]