# Generated by Django 4.2.5 on 2024-03-04 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ikea', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='url',
        ),
    ]