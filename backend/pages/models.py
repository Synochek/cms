from django.db import models


class Page(models.Model):
    '''Форма обратной связи'''
    title = models.CharField('Название', max_length=30)  # Автор письма
    text = models.TextField('Текст', max_length=2000)
    active = models.BooleanField('Активность', default=True)
    template = models.CharField('Активность',  max_length=200, default='page/index.html')
    slug = models.SlugField('url', max_length=60)

    def __str__(self):  # Что будет возвращаться при вызове экземпляра класса
        return self.title

    class Meta:  # Как будут именоваться в Джанго наши статьи
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
