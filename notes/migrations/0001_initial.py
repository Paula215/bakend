# Generated by Django 4.1.6 on 2023-02-23 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipe', models.CharField(blank=True, max_length=256)),
                ('name', models.CharField(blank=True, max_length=256)),
                ('description', models.TextField(blank=True, max_length=256)),
            ],
            options={
                'verbose_name': 'Note',
                'verbose_name_plural': 'Notes',
            },
        ),
    ]