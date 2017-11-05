from django.conf.urls import url, include

from races_app.api.v1.auth_resource import AuthResource
from races_app.api.v1.bet_resource import BetResource
from races_app.api.v1.race_resource import RaceResource

urlpatterns = [
    url(r'^/races/', include(RaceResource.urls())),
    url(r'^/bet/', include(BetResource.urls())),
    url(r'^/auth/', include(AuthResource.urls()))
]