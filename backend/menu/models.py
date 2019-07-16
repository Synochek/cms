from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Menu(models.Model):
    '''Форма обратной связи'''
    name = models.CharField('Название', max_length=30)  # Автор письма
    is_auth = models.BooleanField('Для зарегистрированныых', max_length=30, default=False)
    active = models.BooleanField('Активность', default=True)

    def __str__(self):  # Что будет возвращаться при вызове экземпляра класса
        return self.name

    class Meta:  # Как будут именоваться в Джанго наши статьи
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class ItemsMenu(MPTTModel):
    '''Форма обратной связи'''
    name = models.CharField('Название на латинице', max_length=30)
    title = models.CharField('Название на кириллице', max_length=30)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    menu = models.ForeignKey(Menu, verbose_name='Меню', on_delete=models.CASCADE)
    status = models.BooleanField('Отображение', default='True')
    is_auth = models.BooleanField('Для залогиненых', default=False)
    anchor = models.CharField('Якорь', max_length=255, null=True, blank=True)
    url = models.CharField('Ссылка на внешний ресурс', max_length=255)
    active = models.BooleanField('Опубликовать', default=True)

    def __str__(self):  # Что будет возвращаться при вызове экземпляра класса
        return self.name

    class Meta:  # Как будут именоваться в Джанго наши статьи
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'