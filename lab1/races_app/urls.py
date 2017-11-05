from django.conf.urls import url, include
from jwt_auth.views import obtain_jwt_token

from races_app.api.auth_resource import AuthResource
from races_app.api.bet_resource import BetResource
from races_app.api.race_resource import RaceResource
from . import views

urlpatterns = [
    url(r'^$', views.SignInFormView.as_view()),
    url(r'^signup/', views.SignUpFormView.as_view()),
    url(r'^home/', views.show_home),
    url(r'^api/races/', include(RaceResource.urls())),
    url(r'^api/bet/', include(BetResource.urls())),
    url(r'^api/auth/', include(AuthResource.urls()))
]
