# Generated by Django 3.1.1 on 2020-12-28 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0003_auto_20201228_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='Fresh', max_length=200, null=True),
        ),
    ]
