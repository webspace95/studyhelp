# Generated by Django 4.0.3 on 2022-04-11 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0006_address_country_address_first_name_address_last_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='country',
        ),
    ]