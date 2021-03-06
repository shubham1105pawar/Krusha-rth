# Generated by Django 3.0.3 on 2020-03-26 18:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('KrishiGyan', '0012_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=50)),
                ('Answer', models.TextField()),
                ('Qid', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
