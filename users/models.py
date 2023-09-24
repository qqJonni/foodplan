from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True)


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    duration = models.CharField(max_length=128, verbose_name='Срок')
    breakfast = models.CharField(max_length=128, verbose_name='Завтраки')
    lunches = models.CharField(max_length=128, verbose_name='Обеды')
    dinner = models.CharField(max_length=128, verbose_name='Ужины')
    dessert = models.CharField(max_length=128, verbose_name='Десерты')
    quantity = models.CharField(max_length=128, verbose_name='Кол-во персон')
    allergies = models.CharField(max_length=128, verbose_name='Аллергии', null=True, blank=True)

    def __str__(self):
        return f'Подписка для {self.user.username}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
