# Generated by Django 3.1.7 on 2021-03-04 05:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allcomment',
            name='delete',
        ),
        migrations.RemoveField(
            model_name='allcomment',
            name='update',
        ),
        migrations.RemoveField(
            model_name='documentspdf',
            name='delete',
        ),
        migrations.RemoveField(
            model_name='imgarea',
            name='delete',
        ),
        migrations.RemoveField(
            model_name='imgarea',
            name='update',
        ),
        migrations.RemoveField(
            model_name='microbusiness',
            name='delete',
        ),
        migrations.RemoveField(
            model_name='microbusiness',
            name='update',
        ),
    ]
