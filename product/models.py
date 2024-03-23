from django.db import models
from backend.constants import Constants
from manufacturer.models import Manufacturer


class ProductType(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=Constants.CHAR_FIELD_MAX_LENGTH.value
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        db_table = 'product_types'

        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'


class Product(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=Constants.CHAR_FIELD_MAX_LENGTH.value,
        db_index=True
    )
    manufacturer = models.ForeignKey(
        verbose_name='Производитель',
        to=Manufacturer,
        on_delete=models.CASCADE,
        related_name='manufacturer_to_product',
        db_index=True
    )
    product_type = models.ForeignKey(
        verbose_name='Тип товара',
        to=ProductType,
        on_delete=models.CASCADE,
        related_name='product_type_to_product'
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=Constants.DECIMAL_FIELD_MAX_DIGITS.value,
        decimal_places=Constants.DECIMAL_FIELD_PLACES.value
    )
    photo = models.CharField(
        verbose_name='Путь до изображения',
        max_length=Constants.TEXT_FIELD_MAX_LENGTH.value
    )
    max_load = models.PositiveSmallIntegerField(
        verbose_name='Максимальный вес'
    )
    power_reserve = models.PositiveSmallIntegerField(
        verbose_name='Запас хода'
    )
    max_speed = models.PositiveSmallIntegerField(
        verbose_name='Максимальная скорость'
    )
    watt_power = models.PositiveIntegerField(
        verbose_name='Мощьность'
    )

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        db_table = 'products'

        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

