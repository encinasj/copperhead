# Generated by Django 3.0.3 on 2020-04-29 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_supplier_delete'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='adress',
            new_name='address',
        ),
    ]
