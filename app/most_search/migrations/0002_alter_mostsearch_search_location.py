# Generated by Django 4.0.1 on 2022-02-10 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('most_search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mostsearch',
            name='search_location',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='search_location'),
        ),
    ]