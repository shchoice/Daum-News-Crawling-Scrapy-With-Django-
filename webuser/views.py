from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password, check_password
from .forms import RegisterForm, LoginForm
from .models import WebUser


class RegisterView(FormView):
    template_name = "webuser/register.html"
    form_class = RegisterForm
    success_url = "/scraping/"

    # 모델 저장되는 부분 분리
    def form_valid(self, form):
        webuser = WebUser(
            email=form.data.get('email'), 
            password=make_password(form.data.get('password')),
            level='user'
        )
        webuser.save()

        return super().form_valid(form)


class LoginView(FormView):
    template_name = "webuser/login.html"
    form_class = LoginForm
    success_url = "/scraping/"

    # 세션 추가
    def form_valid(self, form):
        self.request.session['user'] = form.data.get('email')

        return super().form_valid(form)


def logout(request):
    if 'user' in request.session:
        del(request.session['user'])

    return redirect('/')
