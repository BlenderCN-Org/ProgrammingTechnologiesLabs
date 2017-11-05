from django.conf.urls import url, include


urlpatterns = [
    url(r'^api/v1/', include('races_app.api.v1.urls')),
]
