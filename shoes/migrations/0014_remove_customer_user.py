# Generated by Django 3.1.1 on 2021-01-05 11:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0013_orderitem_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]