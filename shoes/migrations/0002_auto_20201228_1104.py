# Generated by Django 3.1.1 on 2020-12-28 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product_img',
            new_name='product_img1',
        ),
        migrations.AddField(
            model_name='product',
            name='product_img2',
            field=models.ImageField(blank=True, default='product.png', null=True, upload_to=''),
        ),
    ]
