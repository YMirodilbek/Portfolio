# Generated by Django 4.0.1 on 2022-04-03 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0032_resume_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='gmail',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='messages',
            name='email',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='name',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='messages',
            name='subject',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
