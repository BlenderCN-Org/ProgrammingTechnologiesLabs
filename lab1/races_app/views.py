from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView

from races_app.forms import SignInForm, SignUpForm
from races_app.models import User


class SignInFormView(View):
    form_class = SignInForm
    template_name = 'auth.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/home/')
        return render(request, self.template_name, {'form': form})


class SignUpFormView(View):
    form_class = SignUpForm
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})


def show_home(request):
    return render(request, 'home.html', {})






