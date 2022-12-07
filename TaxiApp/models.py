from django.db import models

class Vehicles(models.Model):
    mark = models.CharField(max_length=50, verbose_name="Марка")
    gosNumber = models.CharField(max_length=9, verbose_name="Гос. номер")
    color = models.CharField(max_length=50, verbose_name="Цвет")
    issueYear = models.DateField(verbose_name="Год выпуска")
    level = models.ForeignKey('Level', null=True, on_delete=models.PROTECT, verbose_name="Класс")

    def __str__(self):
        return self.gosNumber

    class Meta:
        verbose_name_plural = 'Автомобили'
        verbose_name = 'Автомобиль'
        ordering = ['-mark'] 

class Level(models.Model):
    name = models.CharField(max_length=6, db_index=True, verbose_name="Класс")
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Классы'
        verbose_name = 'Класс'
        ordering = ['name']

class Order(models.Model):
    dateTime = models.DateTimeField(max_length=50, verbose_name="Дата и время")
    departure = models.CharField(max_length=50, verbose_name="Адрес отправления")
    destination = models.CharField(max_length=50, verbose_name="Предположительный адрес назначения")
    passangerNumber = models.IntegerField(verbose_name="Количество пасажиров")
    length = models.FloatField(verbose_name="Ориентировочная длина маршрута")
    driver = models.ForeignKey('Driver', null=True, on_delete=models.PROTECT, verbose_name='Водитель')
    
    class Meta:
        verbose_name_plural = 'Заказы'
        verbose_name = 'Заказ'
        ordering = ['id']

class Driver(models.Model):
    surname = models.CharField(max_length=50, verbose_name="Фамилия")
    name = models.CharField(max_length=50, verbose_name="Имя")
    lastName = models.CharField(max_length=50, verbose_name="Отчество")
    birthDate = models.DateField(verbose_name="Дата рождения")
    inn = models.IntegerField(verbose_name="ИНН")
    serno = models.CharField(max_length=15, verbose_name="Серно паспорта")
    vehicle = models.ForeignKey('Vehicles', null=True, on_delete=models.PROTECT, verbose_name='Автомобиль')
    
    def __str__(self):
        return self.surname

    class Meta:
        verbose_name_plural = 'Водители'
        verbose_name = 'Водитель'
        ordering = ['surname']
