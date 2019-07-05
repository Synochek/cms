from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.views import View
from .models import Post, Comment, Category


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
        comments = Comment.objects.filter(post=models)
        print(comments)
        return render(request, 'blog/postfull.html', {'post_full': models, 'comments_topic': comments})
