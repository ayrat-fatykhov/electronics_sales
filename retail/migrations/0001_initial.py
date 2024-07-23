# Generated by Django 4.2.14 on 2024-07-22 16:03

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('model', models.CharField(max_length=255, verbose_name='модель')),
                ('release_date', models.DateField(verbose_name='дата выхода продукта на рынок')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='название')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='почта')),
                ('country', models.CharField(max_length=255, verbose_name='страна')),
                ('city', models.CharField(max_length=255, verbose_name='город')),
                ('street', models.CharField(blank=True, max_length=255, null=True, verbose_name='улица')),
                ('house_number', models.CharField(blank=True, max_length=100, null=True, verbose_name='номер дома')),
                ('element_network', models.CharField(choices=[('1', 'Завод'), ('2', 'Розничная сеть'), ('3', 'Индивидуальный предприниматель')], max_length=1, verbose_name='звено сети')),
                ('debt', models.FloatField(verbose_name='задолженность перед поставщиком')),
                ('created_to', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(2)], verbose_name='уровень')),
                ('products', models.ManyToManyField(to='retail.product', verbose_name='продукты')),
                ('provider', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='retail.link', verbose_name='поставщик')),
            ],
            options={
                'verbose_name': 'звено',
                'verbose_name_plural': 'звенья',
            },
        ),
    ]