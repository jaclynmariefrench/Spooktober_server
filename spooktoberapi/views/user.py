from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User

class UserView(ViewSet):
    """
    """

    def retrieve(self, request, pk=None):
            """Handle GET requests for single user

            Returns:
                Response -- JSON serialized user instance
            """
            try:
                user = User.objects.get(pk=pk)
                serializer = UserSerializer(user, context={'request': request})
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as ex:
                return HttpResponseServerError(ex)


    def list(self, request):
            """Handle GET requests to games resource

            Returns:
                Response -- JSON serialized list of games
            """
            users = User.objects.all()

            serializer = UserSerializer(
                users, many=True, context={'request': request})
            return Response(serializer.data)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for users

    Arguments:
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'email')
        depth = 1