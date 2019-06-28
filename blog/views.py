from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Post


class PostList(View):  # as_View запускает нужный метод класса с таким же именем, как имя метода
    def get(self, request):
        posts = Post.objects.all()
        print(posts)
        return render(request, 'blog/postlist.html', {'post_list': posts})
