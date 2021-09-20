"""View module for handling requests about the movie waitlist"""
from spooktoberapi.models.movie_tv import Movie_Tv
from spooktoberapi.models.spooktober_user import SpooktoberUser
from spooktoberapi.models.waitlist import Waitlist
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers


class WaitlistView(ViewSet):
    """Calendar View"""

    def create(self, request):
        """Handle POST operations for waitlist

        Returns:
            Response -- JSON serialized movie save instance
        """


        waitlist = Waitlist()
        waitlist.spooktober_user = SpooktoberUser.objects.get(user=request.auth.user)
        waitlist.movie_tv = Movie_Tv.objects.get(pk=request.data["movie_tv"])


        try:
            waitlist.save()
            serializer = WaitlistSerializer(waitlist, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Handle GET requests for waitlist movie

        Returns:
            Response -- JSON serialized game instance
        """
        try:
            waitlist = Waitlist.objects.get(pk=pk)
            serializer = WaitlistSerializer(waitlist, context={'request': request})
            return Response(serializer.data)
        except Waitlist.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single waitlist movie

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            waitlist = Waitlist.objects.get(pk=pk)
            waitlist.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except Waitlist.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request):
        """Handle GET requests to full waitlist list

        Returns:
            Response -- JSON serialized list of events
        """
        # waitlist_list = Waitlist.objects.all()
        spooktober_user = SpooktoberUser.objects.get(user=request.auth.user)
        waitlist_list = Waitlist.objects.filter(
        spooktober_user=spooktober_user)


        serializer = WaitlistSerializer(
            waitlist_list, many=True, context={'request': request})
        return Response(serializer.data)



class SpooktoberUserSerializer(serializers.ModelSerializer):
    """JSON serializer for event host's related Django user"""
    class Meta:
        model = SpooktoberUser
        fields = ['user']


class MovieTvSerializer(serializers.ModelSerializer):
    """JSON serializer for games"""
    class Meta:
        model = Movie_Tv
        fields = ('id', 'title')

class WaitlistSerializer(serializers.ModelSerializer):
    """JSON serializer for waitlist"""
    movie_tv = MovieTvSerializer(many=False)
    spooktober_user = SpooktoberUserSerializer(many=False)

    class Meta:
            model = Waitlist
            fields = ['id', 'movie_tv', 'spooktober_user']
            depth= 1