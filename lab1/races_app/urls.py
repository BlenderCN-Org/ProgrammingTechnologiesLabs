from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.SignInFormView.as_view()),
    url(r'^signup/', views.SignUpFormView.as_view()),
    url(r'^home/', views.show_home),
]
