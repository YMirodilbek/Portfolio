# Generated by Django 4.0.1 on 2022-03-03 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_bio_text2_bio_text3'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('city', models.CharField(max_length=80)),
                ('data', models.DateTimeField()),
                ('title', models.CharField(max_length=798)),
                ('text', models.TextField()),
            ],
        ),
    ]
