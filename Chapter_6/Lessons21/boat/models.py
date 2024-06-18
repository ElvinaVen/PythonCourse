from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Owner(models.Model):
    name = models.CharField(max_length=20, verbose_name="имя")
    email = models.EmailField(verbose_name="email", unique=True)

    def __str__(self):
        return f'{self.name} - {self.email}'

    class Meta:
        verbose_name = "владелец"
        verbose_name_plural = "владельцы"


class Boat(models.Model):
    name = models.CharField(max_length=50, verbose_name="название")
    year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name="год выпуска")
    owner = models.ForeignKey(Owner, verbose_name="владелец", on_delete=models.CASCADE)
    price = models.IntegerField(**NULLABLE, verbose_name="цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "лодка"
        verbose_name_plural = "лодки"


class BoatHistory(models.Model):
    boat = models.ForeignKey(Boat, on_delete=models.CASCADE, verbose_name="лодка")
    start_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name="владел c")
    stop_year = models.PositiveSmallIntegerField(**NULLABLE, verbose_name="владел по")
    owner = models.ForeignKey(Owner, verbose_name="владелец", on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.boat} - {self.start_year} - {self.stop_year}'

    class Meta:
        verbose_name = "история"
        verbose_name_plural = "истории"

