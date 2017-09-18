from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.views import View

from races_app.models import Race, Participation


class SignInFormView(View):
    form_class = AuthenticationForm
    template_name = 'auth.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=raw_password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/home/')
        return render(request, self.template_name, {'form': form})


class SignUpFormView(View):
    form_class = UserCreationForm
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/home/')
        return render(request, self.template_name, {'form': form})


@login_required
def show_home(request):
    races = Race.objects.filter().order_by('track')
    print(races.get().horses)
    return render(request, 'races_list.html', {'races': races})






