from django.urls import path
from .views import *

urlpatterns = [
    path('', FeedbackPage.as_view(), name='feedback_page'),
]
