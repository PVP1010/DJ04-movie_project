# Создание модели Film

from django.db import models

class Film(models.Model):
    title = models.CharField('Название фильма', max_length=100)
    description = models.TextField('Описание фильма')
    review = models.TextField('Отзыв')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'