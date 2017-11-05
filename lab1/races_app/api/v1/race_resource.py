from restless.preparers import FieldsPreparer, SubPreparer, CollectionSubPreparer

from races_app.api.v1.base_resource import BaseResource
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
        if 'skip' in self.request.GET:
            skip = int(self.request.GET['skip'])
        else:
            skip = 0
        if 'count' in self.request.GET:
            count = int(self.request.GET['count'])
        else:
            count = 10

        return Race.objects.all()[skip: skip + count]

    def detail(self, pk):
        return Race.objects.get(id=pk)

    def wrap_list_response(self, data):
        return {
            "races": data
        }
