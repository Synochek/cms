from django.db import models

from django.utils import timezone

from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
from django.contrib.auth.models import User


class Category(MPTTModel):
    '''Категории статей'''
    name = models.CharField('название', max_length=40)
    active = models.BooleanField('Опубликовать', default=True)
    slug = models.SlugField('url', max_length=60)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):  # Что будет возвращаться при вызове экземпляра класса
        return self.name

    class Meta:  # Как будут именоваться в Джанго наши статьи
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Tag(models.Model):
    '''Модель тегов к статье'''
    name = models.CharField('название', max_length=40)
    slug = models.SlugField('url', max_length=60)

    def __str__(self):  # Что будет возвращаться при вызове экземпляра класса
        return self.name

    class Meta:  # Как будут именоваться в Джанго наши статьи
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Post(models.Model):
    '''Модель статей'''
    title = models.CharField('Заголовок', max_length=100)
    sub_title = models.CharField('Подзаголовок', max_length=200)
    mini_text = models.TextField('Превью статьи', max_length=600)
    text = models.TextField('Текст статьи')
    created = models.DateTimeField('Дата создания статьи', auto_now_add=True)  # Второй аргумент: идет автозаполнение
    # времени и даты когда мы вносим запись в БД
    publish_date = models.DateTimeField('Дата публикации', default=timezone.now)  # 2 аргумент: автозаполнение даты
    # если мы не выьрали ничего
    active = models.BooleanField('Публикация', default=True)  # Галочка да/нет
    sort = models.PositiveIntegerField('Сортировка статей', default=500)  # Сортировка как в Битриксе,
    # только положительные чисоа
    view = models.PositiveIntegerField('Просмотрено', default=0)
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_NULL, null=True)
    # Последние два артумента означают, что при удалении категория будет становиться в нулл, последняя делает
    # нулл возможным
    slug = models.SlugField('url', max_length=60, default='')

    def __str__(self):  # Что будет возвращаться при вызове экземпляра класса
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'category': self.category.slug, 'slug': self.slug})

    class Meta:  # Как будут именоваться в Джанго наши статьи
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created']  # Фильтр, который можно прописать в модели по умолчанию


class Comment(models.Model):
    '''Комментарии под статьей'''
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)  # Выводит пользователей
    # с помощью встроенной модели Джанго "User"
    # Также после добавления этого не в самом начале нужно использовать костыльный метод с null=True
    text = models.TextField('текст комментария', max_length=800)
    post = models.ForeignKey(Post, verbose_name='Пост', on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField('Дата добавления', auto_now_add=True)
    moderation = models.BooleanField('Разрешена модерация', default=True)

    def __str__(self):  # Что будет возвращаться при вызове экземпляра класса
        return self.text

    class Meta:  # Как будут именоваться в Джанго наши статьи
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
