"""View module for handling requests about movies_tv"""
from spooktoberapi.models.era import Era
from spooktoberapi.models.spirit import Spirit
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

class EraSearchView(ViewSet):
    """Search parameters"""
    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single Era
        Returns:
            Response -- JSON serialized game instance
        """
        try:

            era = Era.objects.get(pk=pk)
            serializer = EraSerializer(
                era, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def list(self, request):
        """Handle GET requests to era resource

        Returns:
            Response -- JSON serialized list of eras
        """
        # Get all game records from the database
        eras = Era.objects.all()

        serializer = EraSerializer(
            eras, many=True, context={'request': request})
        return Response(serializer.data)

class SpiritSearchView(ViewSet):
    """Search parameters"""
    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single spirit
        Returns:
            Response -- JSON serialized game instance
        """
        try:

            spirit = Spirit.objects.get(pk=pk)
            serializer = EraSerializer(
                spirit, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as ex:
            return HttpResponseServerError(ex)
    
    def list(self, request):
        """Handle GET requests to spirit resource

        Returns:
            Response -- JSON serialized list of eras
        """
        # Get all game records from the database
        spirits = Spirit.objects.all()

        serializer = SpiritSerializer(
            spirits, many=True, context={'request': request})
        return Response(serializer.data)

class EraSerializer(serializers.ModelSerializer):
    """JSON serializer for Eras

    Arguments:
        
    """
    class Meta:
        model = Era
        fields = ('id', 'label')

class SpiritSerializer(serializers.ModelSerializer):
    """JSON serializer for Spirit

    Arguments:
        
    """
    class Meta:
        model = Spirit
        fields = ('id', 'label')