# Generated by Django 3.1.1 on 2021-01-05 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0010_auto_20210103_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
