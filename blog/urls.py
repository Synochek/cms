from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:category>/', PostCategory.as_view()),
    path('post/<int:pk>/', PostFull.as_view(), name='post_detail'),
    path('', PostList.as_view(), name='home_page'),
]