"""View module for handling requests about events"""
from spooktoberapi.models.movie_tv import Movie_Tv
from spooktoberapi.models.calendar import UserCal
from spooktoberapi.models.spooktober_user import SpooktoberUser
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers


class CalendarView(ViewSet):
    """Calendar View"""

    def create(self, request):
        """Handle POST operations for events

        Returns:
            Response -- JSON serialized event instance
        """


        cal_events = UserCal()
        cal_events.spooktober_user = SpooktoberUser.objects.get(user=request.auth.user)
        cal_events.movie_tv = Movie_Tv.objects.get(pk=request.data["movie_tv"])
        cal_events.all_day = request.data["all_day"]
        cal_events.start = request.data["start"]
        cal_events.end = request.data["end"]


        try:
            cal_events.save()
            serializer = CalEventSerializer(cal_events, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single event

        Returns:
            Response -- JSON serialized game instance
        """
        try:
            cal_event = UserCal.objects.get(pk=pk)
            serializer = CalEventSerializer(cal_event, context={'request': request})
            return Response(serializer.data)
        except UserCal.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single cal_event

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            cal_event = UserCal.objects.get(pk=pk)
            cal_event.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except UserCal.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to events resource

        Returns:
            Response -- JSON serialized list of events
        """
        cal_events = UserCal.objects.all()
        # current_user = SpooktoberUser.objects.get(user=request.auth.user)
        # current_user.cal_events = UserCal.objects.filter(spooktober_user=current_user)
        
        for cal_event in cal_events:
            cal_event.title = cal_event.movie_tv.title

        # Support filtering events by game
        movie_tv = self.request.query_params.get('movieTv', None)
        if movie_tv is not None:
            cal_events = cal_events.filter(movie_tv__id=type)

        serializer = CalEventSerializer(
            cal_events, many=True, context={'request': request})
        return Response(serializer.data)



class SpooktoberCalSerializer(serializers.ModelSerializer):
    """JSON serializer for event host's related Django user"""
    class Meta:
        model = SpooktoberUser
        fields = ['user']


class MovieTvSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    class Meta:
        model = Movie_Tv
        fields = ('id',)

class CalEventSerializer(serializers.ModelSerializer):
    """JSON serializer for events"""
    movie_tv = MovieTvSerializer(many=False)

    class Meta:
            model = UserCal
            fields = ['id', 'movie_tv', 'spooktober_user', 'all_day', 'start', 'end', 'title']