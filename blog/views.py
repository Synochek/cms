from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def home(request):  # Аргумент передает сам Django из URL. В нем содержится вся инфа из Form Data, которую передает клиент
    print(f'Current method is: {request.method}')
    return HttpResponse(f'Hi, {request.user}')


class PostList(View):
    def get(self, request):
        return HttpResponse('Hi, View')
