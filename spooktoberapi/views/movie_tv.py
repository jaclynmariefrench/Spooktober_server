"""View module for handling requests about movies_tv"""
from spooktoberapi.models.movie_tv import Movie_Tv
from spooktoberapi.models.supernatural import Supernatural

from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status


class MovieTvView(ViewSet):
    """Movies and Tv"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single show
        Returns:
            Response -- JSON serialized game instance
        """
        try:

            movie_tv = Movie_Tv.objects.get(pk=pk)
            serializer = MovieTvSerializer(
                movie_tv, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to games resource

        Returns:
            Response -- JSON serialized list of games
        """
        # Get all game records from the database
        movies_tvs = Movie_Tv.objects.all()

        # Support filtering games by category
        #    http://localhost:8000/games?category=1
        #
        # That URL will retrieve all tabletop games
        supernatural = self.request.query_params.get('supernatural', None)
        if supernatural is not None:
            movies_tvs = Movie_Tv.filter(supernatural__id=supernatural)

        serializer = MovieTvSerializer(
            movies_tvs, many=True, context={'request': request})
        return Response(serializer.data)


class MovieTvSerializer(serializers.ModelSerializer):
    """JSON serializer for Movies and Tv shows

    Arguments:
        serializer category
    """
    class Meta:
        model = Movie_Tv
        fields = ('id', 'title', 'genre', 'subGenre', 'spirit', 'era', 'isMovie', 'isNostalgic',
                  'isMagic', 'isTimBurton', 'isStopMotion', 'imdb_img', 'imdb_rating', 'supernatural')
        depth = 1
