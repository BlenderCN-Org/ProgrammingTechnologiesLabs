from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from races_app.forms import LogInForm


def show_auth(request):
    form = LogInForm()
    return render(request, 'auth.html', {'form': form})


def show_home(request):
    return render(request, 'home.html', {})


def login(request):
    print('login')
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/home/')

    else:
        return HttpResponseRedirect('/')





