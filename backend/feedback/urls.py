from django.urls import path
from .views import *

urlpatterns = [
    path('feedback', FeedbackPage.as_view(), name='feedback_page'),
]
