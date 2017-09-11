from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.show_auth),
    url(r'^login/', views.login),
    url(r'^home/', views.show_home),
]
