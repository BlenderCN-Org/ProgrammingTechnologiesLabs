from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_auth),
    url(r'^login/', views.login),
    url(r'^signup/', views.show_sign_up),
    url(r'^home/', views.show_home),
]
