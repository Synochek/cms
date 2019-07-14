from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import View
from django.shortcuts import redirect
from .models import Post, Comment, Category
from .forms.forms import CommentForm
from django.contrib import messages


class PostList(View):  # Выводит найденные посты в списке
    def get(self, request):
        posts = Post.objects.filter(category__active=True)  # Фильтруется сначала по активности,
        # а потом в обратном порядке
        return render(request, 'blog/postlist.html', {'post_list': posts})


class PostCategory(View):
    def get(self, request, category):
        posts = Post.objects.filter(category__slug=category, category__active=True)  # Найди категории
        # по определенному слагу, которые при этом активны
        print(posts)
        if posts.exists():
            return render(request, 'blog/postlist.html', {'post_list': posts})
        else:
            return HttpResponse('The category is doesn\'t exists')  # Выводит сообщение что не найдено


class PostFull(View):
    def get(self, request, category, slug):
        models = Post.objects.get(slug=slug)
        comments = Comment.objects.filter(post=models, moderation=True)
        form = CommentForm()
        # print('наш GET: ' + str(form))
        return render(request, 'blog/postfull.html', {'post_full': models, 'comments_topic': comments, 'form': form})

    def post(self, request, category, slug):  # Заполняется форма из HTML <form>, 'text' - это name формы в html

        # print('Автор: ' + str(request.POST.get('user')))
        # print('Комментарий: ' + str(request.POST.get('text')))
        # print('Данные Пост: ' + str(request.POST))

        form = CommentForm(request.POST)  # теперь формы содержит все поля нашей модели, на которую ссылается этот класс
        # из форм.
        if form.is_valid():  # Проверка на валидность формы (наличие символов)
            form = form.save(commit=False)  # Форму сейчас не нужно сохранять. Мы хотим поработать с данными. Без этого
            # поля у формы не будет привязки к посту
            form.post = Post.objects.get(slug=slug)
            form.user = request.user
            form.save()  # Сохраняет запись с полями в БД данные, положенные в форму. Они основаны на модели
            # Comment.objects.create(author=request.POST.get('author'), text=request.POST.get('text'), post=Post.objects.get(slug=slug))
            # Это то, что происходит вместо закомментарованного кода, который реализуется без forms
            messages.add_message(request, settings.MY_INFO, 'Ваш комментарий вскоре будет проверен модератором')
        else:
            messages.add_message(request, settings.MY_INFO, 'Ошибка')
        return redirect(request.path)
# Или redirect(request.path) - просто перенаправить на эту же страницу



