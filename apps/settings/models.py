from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length = 255,
        verbose_name = "Название сайта",
    )
    description = models.TextField(
        verbose_name = "Описание"
    )
    email = models.EmailField(
        verbose_name = "Почта"
    )
    address = models.CharField(
        max_length = 255,
        verbose_name = "Адрес",
        blank = True, null = True
    )
    phone = models.CharField(
        max_length = 100,
        verbose_name = "Телефонный номер",
        blank = True, null = True
    )
    logo = models.ImageField(
        upload_to = "logo/",
        verbose_name = "Логотип"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"