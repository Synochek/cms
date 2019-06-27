from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Post

class PostList(View):
    def get(self, request):
        posts = Post.object
