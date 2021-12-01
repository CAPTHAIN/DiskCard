# Generated by Django 3.2.9 on 2021-11-25 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_sum',
            field=models.FloatField(blank=True, verbose_name='Сумма'),
        ),
        migrations.AlterField(
            model_name='card',
            name='is_active',
            field=models.BooleanField(blank=True, default=True, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='card',
            name='use_date',
            field=models.DateField(blank=True, verbose_name='Дата использования'),
        ),
    ]