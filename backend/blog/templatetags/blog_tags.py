from django import template

from backend.blog.models import Category

register = template.Library()


@register.inclusion_tag('blog/tags/category.html', takes_context=True)  # Контекст означает передачу request
# в этот шаблон. В шаблонах с темплейт-тегом приходится так делать
def category_list(context, publish=True):  # В функцию передали контекст (request)
    # template_tag вывода категорий
    category = Category.objects.filter(active=publish)  # Задается с помощью аргумента значение
    return {'category_list': category, 'user': context['user']}  # Ключ 'user' передает контекст (request) с параметром
    # user. Поэтому в шаблоне мы обращаемся к нему как {% if user.is_authenticated %}


@register.filter()
def comment_padding(value):
    # Фильтр сдвига комментария
    return int(value / 2) == float(value / 2)  # Операция, вычиляющая: четное или нечетное число
    # комментария в данный момент
