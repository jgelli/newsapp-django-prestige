# Generated by Django 3.2.9 on 2021-11-09 18:57

from django.db import migrations, models
import functions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertising',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('image', models.ImageField(upload_to=functions.path_and_rename)),
            ],
        ),
    ]
