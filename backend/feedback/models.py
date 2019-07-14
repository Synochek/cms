from django.db import models


class Feedback(models.Model):
    '''Форма обратной связи'''
    name = models.CharField('Имя', max_length=30)  # Автор письма
    email = models.EmailField('Почта', max_length=30, null=True)  # Убрал EmailField для надежности
    phone = models.CharField('Телефон', max_length=14, blank=True)
    text = models.TextField('Текст формы', max_length=800)
    created = models.DateTimeField('Дата добавления', auto_now_add=True)

    def __str__(self):  # Что будет возвращаться при вызове экземпляра класса
        return self.text

    class Meta:  # Как будут именоваться в Джанго наши статьи
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'
