from django.urls import path
from .views import *

urlpatterns = [
    path('<slug:category>/post/<slug:slug>/', PostFull.as_view(), name='post_detail'),
    path('<slug:category>/', PostCategory.as_view(), name='category_page'),
    path('feedback', FeedbackPage.as_view(), name='feedback_page'),
    path('', PostList.as_view(), name='home_page'),
]
