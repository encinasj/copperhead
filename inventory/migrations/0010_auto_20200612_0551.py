# Generated by Django 3.0.7 on 2020-06-12 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20200612_0545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='img',
            field=models.ImageField(null=True, upload_to='inventory/media/articles'),
        ),
    ]
