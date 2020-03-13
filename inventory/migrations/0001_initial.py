# Generated by Django 3.0.3 on 2020-03-10 20:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('delete', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Brand',
                'verbose_name_plural': 'Brand',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('delete', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
            },
        ),
        migrations.CreateModel(
            name='MicroBusiness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img', models.ImageField(upload_to='inventory/mb')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('delete', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'MicroBusiness',
                'verbose_name_plural': 'MicroBusinesses',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_company', models.CharField(max_length=60)),
                ('name_contact', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=12)),
                ('adress', models.CharField(max_length=60)),
                ('cel_phone', models.CharField(max_length=12)),
                ('web', models.URLField()),
                ('email', models.EmailField(max_length=254)),
                ('comments', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('delete', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Supplier',
                'verbose_name_plural': 'Suppliers',
            },
        ),
        migrations.CreateModel(
            name='TypeArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('delete', models.DateField(auto_now=True)),
            ],
            options={
                'verbose_name': 'TypeArticle',
                'verbose_name_plural': 'TypeArticles',
            },
        ),
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='')),
                ('img', models.ImageField(upload_to='inventory/articles')),
                ('quantity', models.DecimalField(decimal_places=3, max_digits=4)),
                ('model', models.CharField(max_length=50)),
                ('coust_buy', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField(blank=True)),
                ('userful_life', models.DateField()),
                ('actual_state', models.CharField(choices=[('N', 'Nuevo'), ('S', 'Semi nuevo'), ('U', 'Usado'), ('O', 'Otros')], max_length=1)),
                ('date_check', models.DateField()),
                ('location', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('delete', models.DateField(auto_now=True)),
                ('fk_brand', models.ManyToManyField(to='inventory.Brand')),
                ('fk_category', models.ManyToManyField(to='inventory.Category')),
                ('fk_microbusiness', models.ManyToManyField(to='inventory.MicroBusiness')),
                ('fk_supplier', models.ManyToManyField(to='inventory.Supplier')),
                ('fk_user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Article',
                'verbose_name_plural': 'Articles',
            },
        ),
    ]
