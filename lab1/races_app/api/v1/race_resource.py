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

    bet_preparer = FieldsPreparer(fields={
        'bet': 'bet',
        'rating': 'rating'
    })

    participant_preparer = FieldsPreparer(fields={
        'id': 'id',
        'horse': SubPreparer('horse', horse_preparer),
        'rating': 'rate',
        'bets': CollectionSubPreparer('bets.all', bet_preparer)
    })



    preparer = FieldsPreparer(fields={
        'id': 'id',
        'title': 'track',
        'organizer': SubPreparer('organizer', organizer_preparer),
        'participants': CollectionSubPreparer('participants.all', participant_preparer)
    })

    def list(self, *args, **kwargs):
        return self.get_page(Race.objects.all())

    def detail(self, pk):
        return Race.objects.get(id=pk)

    def wrap_list_response(self, data):
        return {
            "races": data
        }
