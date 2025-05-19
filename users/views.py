import os

from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from dotenv import load_dotenv

from .forms import CustomUserCreationForm


load_dotenv(override=True)


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в интернет-магазин BystrovStore!'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        from_email = os.getenv('EMAIL_HOST_USER')
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)
