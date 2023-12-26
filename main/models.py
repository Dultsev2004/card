import uuid
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    avatar = models.ImageField(upload_to="avatar/", verbose_name='Аватарка')

    def __str__(self):
        return self.username


class Services(models.Model):
    title = models.CharField(max_length=64, verbose_name='Заголовок')
    description = models.TextField(max_length=256, verbose_name='Описание')
    image = models.ImageField(upload_to="images/", verbose_name='Изображение')
    code = models.TextField(max_length=64, verbose_name='Код товара')

    def __str__(self):
        return self.title


class ServicesDetail(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,)
    service = models.ForeignKey('Services', on_delete=models.RESTRICT, null=True)

    def get_absolute_url(self):
        return reverse('service-detail', args=[str(self.id)])


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.service.title}"