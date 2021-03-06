# Generated by Django 3.2.9 on 2021-11-23 16:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('series', models.PositiveIntegerField(verbose_name='Серия')),
                ('amount', models.PositiveIntegerField(verbose_name='Номер')),
                ('release_date', models.DateField(auto_now_add=True, verbose_name='Дата выпуска')),
                ('end_date', models.DateField(verbose_name='Дата окончания активности')),
                ('use_date', models.DateField(verbose_name='Дата использования')),
                ('card_sum', models.FloatField(verbose_name='Сумма')),
                ('is_active', models.BooleanField(default=True, verbose_name='Статус')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.card', verbose_name='Карта')),
            ],
        ),
    ]
