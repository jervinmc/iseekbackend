# Generated by Django 4.0.1 on 2022-02-10 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('most_demand', '0002_remove_mostdemand_search_job_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mostdemand',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='quantity'),
        ),
    ]
