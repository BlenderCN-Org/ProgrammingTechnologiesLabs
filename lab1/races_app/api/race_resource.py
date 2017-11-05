from restless.preparers import FieldsPreparer, SubPreparer, CollectionSubPreparer

from races_app.api.base_resource import BaseResource
from races_app.models import Race


class RaceResource(BaseResource):

    horse_preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name'
    })

    organizer_preparer = FieldsPreparer(fields={
        'id': 'id',
        'name': 'name'
    })

    participant_preparer = FieldsPreparer(fields={
        'id': 'id',
        'horse': SubPreparer('horse', horse_preparer),
        'rating': 'rate'
    })

    preparer = FieldsPreparer(fields={
        'id': 'id',
        'title': 'track',
        'organizer': SubPreparer('organizer', organizer_preparer),
        'participants': CollectionSubPreparer('participants.all', participant_preparer)
    })

    def list(self, *args, **kwargs):
        skip = int(self.request.GET['skip'])
        count = int(self.request.GET['count'])
        return Race.objects.all()[skip: skip + count]

    def detail(self, pk):
        return Race.objects.get(id=pk)

    def wrap_list_response(self, data):
        return {
            "races": data
        }
