from django.db import models


class Card(models.Model):
    series = models.PositiveIntegerField(verbose_name='Серия')
    amount = models.PositiveIntegerField(verbose_name='Номер')
    release_date = models.DateField(auto_now_add=True, verbose_name='Дата выпуска')
    end_date = models.DateField(verbose_name='Дата окончания активности')
    use_date = models.DateField(verbose_name='Дата использования', blank=True, null=True)
    card_sum = models.FloatField(verbose_name='Сумма', blank=True, null=True, default=0)
    is_active = models.CharField(max_length=255, default='Активна', verbose_name='Статус')

    def __str__(self):
        return str(self.series)


class Item(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название товара')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, verbose_name='Карта')

    def __str__(self):
        return self.name


