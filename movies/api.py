from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from django.shortcuts import get_object_or_404
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

    def detail(self, pk):
        return get_object_or_404(Movie, pk=pk)

    def is_authenticated(self):
        return True
