# Generated by Django 3.1.1 on 2021-01-05 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0017_auto_20210105_1756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
    ]
