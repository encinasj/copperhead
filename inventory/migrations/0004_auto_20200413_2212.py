# Generated by Django 3.0.3 on 2020-04-13 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_remove_category_delete'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brand',
            name='delete',
        ),
        migrations.RemoveField(
            model_name='microbusiness',
            name='delete',
        ),
        migrations.RemoveField(
            model_name='microbusiness',
            name='img',
        ),
        migrations.RemoveField(
            model_name='typearticle',
            name='delete',
        ),
    ]