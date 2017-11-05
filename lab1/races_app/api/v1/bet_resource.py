import json

from restless.preparers import FieldsPreparer
from restless.resources import skip_prepare

from races_app.api.v1.base_resource import BaseResource
from races_app.models import Bet, Participation


class BetResource(BaseResource):

    preparer = FieldsPreparer(fields={
        'id': 'id',
        'bet': 'bet',
        'rating': 'rating',
        'participant_id': 'participant_id',
        'race_date': 'participant.race.date',
        'horse_name': 'participant.horse.name',
        'result': 'result'
    })

    def list(self, *args, **kwargs):
        return Bet.objects.filter(client_id=self.request.client.id).all()

    @skip_prepare
    def create(self, *args, **kwargs):
        body = json.loads(self.request.body.decode("utf-8"))
        print(body)
        bet = Bet(bet=body['bet'], rating=body['rating'])
        participant = Participation.objects.get(id=body['participant_id'])
        bet.participant = participant
        user = self.request.client
        bet.client = user
        bet.save()

        return {
            'result': True
        }
