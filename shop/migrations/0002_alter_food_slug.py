# Generated by Django 5.0 on 2023-12-17 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
