# Generated by Django 3.1.1 on 2021-01-05 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0023_auto_20210105_2310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]
