from django.db import models

from django.db import models

class Buyer(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Имя покупателя")
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Баланс")
    age = models.PositiveIntegerField(verbose_name="Возраст")

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название игры")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    size = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Размер файла (ГБ)")
    description = models.TextField(verbose_name="Описание")
    age_limited = models.BooleanField(default=False, verbose_name="Возрастное ограничение 18+")
    buyers = models.ManyToManyField("Buyer", related_name="games", verbose_name="Покупатели")

    def __str__(self):
        return self.title
