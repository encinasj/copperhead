# Generated by Django 3.0.7 on 2021-02-02 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0025_articles_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='articles/'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes/'),
        ),
    ]
