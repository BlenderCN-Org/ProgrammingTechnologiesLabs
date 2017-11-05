from restless.constants import OK
from restless.dj import DjangoResource


class BaseResource(DjangoResource):

    def build_response(self, data, status=OK):
        wrapped_data = wrapped_response(self.serializer.deserialize(data), status)
        serialized_wrapped_data = self.serializer.serialize(wrapped_data)
        return super().build_response(serialized_wrapped_data, status)


def wrapped_response(data, status):
    return {
        'data': data,
        'status': status,
    }

