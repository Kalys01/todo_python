from django.db import models

class ToDo(models.Model):
    text = models.CharField('Заголовок', max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)


class Book(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    subtitle = models.CharField('Подзаголовок', max_length=150)
    description = models.TextField('Описание', max_length=10000)
    price = models.IntegerField('Цена')
    genre = models.CharField('Жанр', max_length=50)
    author = models.CharField('Автор', max_length=80)
    years = models.DateField('Год_выхода_книг', auto_now_add=False)
    date = models.DateField('Дата', auto_now_add=True)
    favorite = models.BooleanField(default=False)

    