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
            auth = JSONWebTokenAuthMixin().authenticate(self.request)
            if auth is not None:
                self.request.client = auth[0]
                return True
            else:
                return False
        except Exception as error:
            print(error)
            return False

    def get_page(self, query_result):
        if 'skip' in self.request.GET:
            skip = int(self.request.GET['skip'])
        else:
            skip = 0
        if 'count' in self.request.GET:
            count = int(self.request.GET['count'])
        else:
            count = 10
        return query_result[skip: skip + count]


def wrapped_response(data, status):
    return {
        'data': data,
        'status': status,
    }


