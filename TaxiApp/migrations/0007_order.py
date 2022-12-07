# Generated by Django 4.1.4 on 2022-12-07 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TaxiApp', '0006_alter_level_options_remove_level_level_level_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateTime', models.DateTimeField(max_length=50, verbose_name='Дата и время')),
                ('departure', models.CharField(max_length=50, verbose_name='Адрес отправления')),
                ('destination', models.CharField(max_length=50, verbose_name='Предположительный адрес назначения')),
                ('passangerNumber', models.IntegerField(verbose_name='Количество пасажиров')),
                ('length', models.FloatField(verbose_name='Ориентировочная длина маршрута')),
                ('serno', models.CharField(max_length=15, verbose_name='Серно паспорта')),
                ('driver', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='TaxiApp.driver', verbose_name='Водитель')),
            ],
            options={
                'verbose_name': 'Заказ',
                'verbose_name_plural': 'Заказы',
                'ordering': ['id'],
            },
        ),
    ]