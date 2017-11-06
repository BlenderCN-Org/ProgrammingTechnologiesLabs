import json

from django.conf.urls import url
from django.contrib.auth.models import User
from jwt_auth.forms import JSONWebTokenForm
from restless.resources import skip_prepare

from races_app.api.v1.base_resource import BaseResource


class AuthResource(BaseResource):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.http_methods.update({
            'sign_in': {
                'POST': 'sign_in_schema',
            },
            'sign_up': {
                'POST': 'sign_up_schema',
            }
        })

    def is_authenticated(self):
        return True

    @skip_prepare
    def sign_in_schema(self):
        try:
            request_json = json.loads(self.request.body.decode("utf-8"))
        except ValueError as error:
            raise error

        credentials = {
            'username': request_json['email'],
            'password': request_json['password']
        }

        form = JSONWebTokenForm(credentials)

        if not form.is_valid():
            raise ValueError(form.errors['__all__'][0])

        return {
            'token': form.object['token']
        }

    @skip_prepare
    def sign_up_schema(self):
        try:
            request_json = json.loads(self.request.body.decode("utf-8"))
        except ValueError as error:
            raise error
        first_name = request_json['first_name']
        last_name = request_json['last_name']
        email = request_json['email']
        password = request_json['password']

        user = User(username=email, first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        user.save()

        credentials = {
            'username': email,
            'password': password
        }

        # return {
        #     "user": user
        # }

        form = JSONWebTokenForm(credentials)

        if not form.is_valid():
            raise ValueError(form.errors['__all__'][0])

        return {
            'token': form.object['token']
        }

    @classmethod
    def urls(cls, name_prefix=None):
        return [
            url(r'^sign_in/$', cls.as_view('sign_in'), name=cls.build_url_name('sign_in', name_prefix)),
            url(r'^sign_up/$', cls.as_view('sign_up'), name=cls.build_url_name('sign_up', name_prefix))
        ]
