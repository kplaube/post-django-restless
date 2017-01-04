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

    def create(self):
        return Movie.objects.create(
            title=self.data['title'],
            description=self.data['description'],
        )

    def is_authenticated(self):
        return True
