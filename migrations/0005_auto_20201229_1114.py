# Generated by Django 3.1.1 on 2020-12-29 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0004_auto_20201228_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='size',
            field=models.CharField(choices=[('US7', 'US7'), ('US8', 'US8'), ('US9', 'US9'), ('US10', 'US10')], default='US8', max_length=200),
        ),
    ]