from django.db import models


class Product(models.Model):

    OTHER = "other"
    SMARTPHONES = "smartphone"
    CLOTHES = 'clothes'
    HOME = 'home'
    COMPUTERS = 'computers'

    CATEGORY_CHOICES = [
        (OTHER, 'разное'),
        (SMARTPHONES, 'смартфоны'),
        (CLOTHES, 'одежда'),
        (HOME, 'товары для дома'),
        (COMPUTERS, 'компьютеры'),
    ]

    name = models.CharField(max_length=100, null=False, verbose_name="Наименование товара")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Описание товара")
    image = models.URLField(verbose_name="Изображение товара")
    category = models.CharField(verbose_name="Категория товара", max_length=10, choices=CATEGORY_CHOICES, default=OTHER)
    remainder = models.PositiveIntegerField(verbose_name="Остаток от товара",)
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Стоимость товара")
