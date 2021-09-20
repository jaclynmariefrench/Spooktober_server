from django.http.response import HttpResponseServerError
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import serializers
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from spooktoberapi.models.spooktober_user import SpooktoberUser

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    name = request.data['name']
    email = request.data['email']
    google_id = request.data['googleId']


    try:
        user = User.objects.get(email=email)
        token = Token.objects.get(user_id=user.id)
        data = {
            'valid': True, 
            'token': token.key 
            }
        return Response(data)

    except User.DoesNotExist:
        user = User.objects.create_user(
            email=email,
            password=google_id,
            username=name,
        )

        spooktober_user = SpooktoberUser.objects.create(
            user=user
        )

        token = Token.objects.create(user_id=spooktober_user.user.id)
        data = {
            'valid': True, 
            'token': token.key
        }
        
        return Response(data)
    
    except Exception as ex:
        return HttpResponseServerError(ex)

