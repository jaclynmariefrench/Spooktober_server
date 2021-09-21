"""View module for handling requests about movies_tv"""
from spooktoberapi.models.movie_tv import Movie_Tv
from spooktoberapi.models.spooktober_user import SpooktoberUser
from rest_framework.decorators import action
from spooktoberapi.models.supernatural import Supernatural
from django.db.models import Q

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

        #     search_text = self.request.query_params.get('q', None)

        #     Movie_Tv.objects.filter(
        #         Q(era__contains=search_text) |
        #         Q(spirit__contains=search_text)
        # )
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
        spooktober_user = SpooktoberUser.objects.get(user=request.auth.user)

        # Support filtering games by category
        #    http://localhost:8000/games?category=1
        #
        # That URL will retrieve all tabletop games
        for movie in movies_tvs:
            movie.added = spooktober_user in movie.user_waitlist.all()
        supernatural = self.request.query_params.get('supernatural', None)
        if supernatural is not None:
            movies_tvs = Movie_Tv.filter(supernatural__id=supernatural)

        serializer = MovieTvSerializer(
            movies_tvs, many=True, context={'request': request})
        return Response(serializer.data)
    @action(methods=['post', 'delete'], detail=True)
    def waitlist(self, request, pk=None):
        """Managing movies to add to waitlist"""
        # Django uses the `Authorization` header to determine
        # which user is making the request to sign up
        spooktober_user = SpooktoberUser.objects.get(user=request.auth.user)
    
        try:
            # Handle the case if the client specifies a movie
            # that doesn't exist
            movie_tv = Movie_Tv.objects.get(pk=pk)
        except Movie_Tv.DoesNotExist:
            return Response(
                {'message': 'Movie does not exist.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # A user wants to add a post to the waitlist
        if request.method == "POST":
            try:
                # Using the attendees field on the event makes it simple to add a gamer to the event
                # .add(gamer) will insert into the join table a new row the gamer_id and the event_id
                movie_tv.user_waitlist.add(spooktober_user)
                return Response({}, status=status.HTTP_201_CREATED)
            except Exception as ex:
                return Response({'message': ex.args[0]})

    # User wants to leave a previously joined event
        elif request.method == "DELETE":
            try:
                # The many to many relationship has a .remove method that removes the gamer from the attendees list
                # The method deletes the row in the join table that has the gamer_id and event_id
                movie_tv.user_waitlist.remove(spooktober_user)
                return Response(None, status=status.HTTP_204_NO_CONTENT)
            except Exception as ex:
                return Response({'message': ex.args[0]})
        


class MovieTvSerializer(serializers.ModelSerializer):
    """JSON serializer for Movies and Tv shows

    Arguments:
        serializer category
    """
    class Meta:
        model = Movie_Tv
        fields = ('id', 'title', 'genre', 'subGenre', 'spirit', 'era', 'isMovie', 'isNostalgic',
                  'isMagic', 'isTimBurton', 'isStopMotion', 'imdb_img', 'imdb_rating', 'supernatural', 'added')
        depth = 1
