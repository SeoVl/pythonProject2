from django.db import models


class Articles(models.Model):
    model = models.CharField('Модель', max_length=50)
    engine = models.CharField('Двигатель', max_length=50)
    speed = models.CharField('Разгон(0-100)', max_length=50)
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.model

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

