# Generated by Django 3.1.1 on 2021-02-07 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0037_contact_positiive'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='positiive',
            new_name='positive',
        ),
    ]
