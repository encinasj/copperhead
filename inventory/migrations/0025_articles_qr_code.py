# Generated by Django 3.0.7 on 2021-02-02 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0024_auto_20210126_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='qr_code',
            field=models.ImageField(blank=True, upload_to='qr_codes'),
        ),
    ]
