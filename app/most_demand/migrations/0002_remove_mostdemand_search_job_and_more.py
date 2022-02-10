# Generated by Django 4.0.1 on 2022-02-10 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('most_demand', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mostdemand',
            name='search_job',
        ),
        migrations.RemoveField(
            model_name='mostdemand',
            name='search_location',
        ),
        migrations.AddField(
            model_name='mostdemand',
            name='category',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='category'),
        ),
    ]
