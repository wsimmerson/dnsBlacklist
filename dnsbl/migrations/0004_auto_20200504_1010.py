# Generated by Django 3.0.5 on 2020-05-04 14:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dnsbl', '0003_trusteddomain'),
    ]

    operations = [
        migrations.AddField(
            model_name='blacklistedip',
            name='last_seen',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='blacklistedip',
            name='ip_address',
            field=models.GenericIPAddressField(unique=True),
        ),
        migrations.AlterField(
            model_name='whitelistedip',
            name='ip_address',
            field=models.GenericIPAddressField(unique=True),
        ),
    ]