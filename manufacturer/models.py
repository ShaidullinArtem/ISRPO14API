from django.db import models

from backend.constants import Constants


class Manufacturer(models.Model):
    name = models.CharField(
        verbose_name='Название',
        max_length=Constants.CHAR_FIELD_MAX_LENGTH.value)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        db_table = 'manufacturers'

        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

