# Generated by Django 3.1.1 on 2021-01-24 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0034_remove_product_product_img5'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
