from jwt_auth.mixins import JSONWebTokenAuthMixin
from restless.constants import OK
from restless.dj import DjangoResource


class BaseResource(DjangoResource):

    def build_response(self, data, status=OK):
        wrapped_data = wrapped_response(self.serializer.deserialize(data), status)
        serialized_wrapped_data = self.serializer.serialize(wrapped_data)
        return super().build_response(serialized_wrapped_data, status)

    def is_authenticated(self):
        try:
            print("checking")
            auth = JSONWebTokenAuthMixin().authenticate(self.request)
            print("get auth")
            print(auth)
            if auth is not None:
                self.request.client = auth[0]
                return True
            else:
                return False
        except Exception as error:
            print(error)
            return False


def wrapped_response(data, status):
    return {
        'data': data,
        'status': status,
    }


