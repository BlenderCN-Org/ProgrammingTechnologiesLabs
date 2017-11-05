from django.conf.urls import url, include

from races_app.api.race_resource import RaceResource
from . import views

urlpatterns = [
    url(r'^$', views.SignInFormView.as_view()),
    url(r'^signup/', views.SignUpFormView.as_view()),
    url(r'^home/', views.show_home),
    url(r'^api/races/', include(RaceResource.urls()))
]
