# Generated by Django 4.1.6 on 2023-02-23 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='customer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='customers.customer'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.TextField(max_length=256),
        ),
        migrations.AlterField(
            model_name='note',
            name='name',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='note',
            name='tipe',
            field=models.CharField(max_length=256),
        ),
    ]
