# Generated by Django 3.0.11 on 2021-08-12 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenge',
            name='cloud_provider',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Cloud Provider'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='cloud_provider_token',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Cloud Provider token'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='cloud_provider_url',
            field=models.URLField(blank=True, null=True, verbose_name='Cloud Provider URL'),
        ),
        migrations.AlterField(
            model_name='challenge',
            name='slack_group',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Slack group'),
        ),
    ]
