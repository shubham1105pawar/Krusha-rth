# Generated by Django 3.0.3 on 2020-03-23 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KrishiGyan', '0009_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
    ]
