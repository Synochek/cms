from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views import View
from django.shortcuts import redirect
from .models import Feedback
from .forms.forms import FeedbackForm
from django.contrib import messages


class FeedbackPage(View):
    def get(self, request):
        forms = FeedbackForm()
        print('наш GET: ' + str(forms))
        return render(request, 'templates/blog/inner_pages/feedback.html', {'forms_list': forms})  # Передаем объект формы

    def post(self, request):
        print('Данные Пост: ' + str(request.POST))

        # Feedback.objects.create(  # Создание формы первым способом, без forms
        #     name=request.POST.get('name'),
        #     email=request.POST.get('email'),
        #     phone=request.POST.get('phone'),
        #     text=request.POST.get('text')
        # )

        form = FeedbackForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)  # Форму сейчас не нужно сохранять. Мы хотим поработать с данными. Без этого
            # поля у формы не будет привязки к посту
            form.save()  # Создание формы первым способом
            messages.add_message(request, settings.FEEDBACK_FORM, 'Ваша форма успешно отправлегна')  # форма на основе
            # формы Миши
        else:
            messages.add_message(request, settings.FEEDBACK_FORM, 'Ошибка')
        return redirect(request.path)
