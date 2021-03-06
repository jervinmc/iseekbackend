# Generated by Django 4.0.1 on 2022-02-09 23:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=255, null=True, verbose_name='email')),
                ('password', models.CharField(blank=True, max_length=255, null=True, verbose_name='password')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, verbose_name='timestamp')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
