# Generated by Django 3.1.1 on 2021-01-17 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0028_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='customer',
        ),
    ]