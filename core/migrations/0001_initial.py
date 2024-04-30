# Generated by Django 5.0.4 on 2024-04-29 17:35

import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Data da criação')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Data da modificação')),
                ('status', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço')),
                ('image', stdimage.models.StdImageField(force_min_size=False, upload_to='products', variations={'thumbnail': (100, 75)})),
                ('slug', models.SlugField(blank=True, editable=False, max_length=100, verbose_name='Slug')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]