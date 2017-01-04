from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from movies.models import Movie


class MovieResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'id': 'id',
        'title': 'title',
        'description': 'description',
    })

    def list(self):
        return Movie.objects.all()
