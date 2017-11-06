from restless.preparers import FieldsPreparer, SubPreparer

from races_app.api.v1.base_resource import BaseResource


class UserResource(BaseResource):

    details_preparer = FieldsPreparer(fields={
        'avatar': 'avatar'
    })

    preparer = FieldsPreparer(fields={
        'id': 'id',
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email',
        'details': SubPreparer('details.first', details_preparer)
    })

    def detail(self):
        return self.request.client
