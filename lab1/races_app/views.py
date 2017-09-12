from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from races_app.forms import LogInForm, SignUpForm


def show_auth(request):
    form = LogInForm()
    return render(request, 'auth.html', {'form': form})


def show_sign_up(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'signup.html', {'form': form})
    else:
        return signup(request)


def show_home(request):
    return render(request, 'home.html', {})


def login(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/home/')
    else:
        return HttpResponseRedirect('/')


def signup(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        return HttpResponseRedirect('/')
    else:
        return JsonResponse({'message': 'error'})




