# Generated by Django 3.1.1 on 2020-12-29 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0005_auto_20201229_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='note',
        ),
    ]
