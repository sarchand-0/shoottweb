# Generated by Django 3.1.1 on 2021-01-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0035_product_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feedback',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]