from django.db import models

class Vehicles(models.Model):
 mark = models.CharField(max_length=50, verbose_name="Номер")
 level = models.CharField(max_length=6, verbose_name="Класс")
 gosNumber = models.CharField(max_length=9, verbose_name="Гос. номер")
 color = models.CharField(max_length=50, verbose_name="Цвет")
 issueYear = models.DateField(verbose_name="Год выпуска")