from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import UserSerializer
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from accounts.models import User
from django.contrib.auth import login, authenticate
from django.http import JsonResponse
import jwt


@permission_classes([AllowAny])
@api_view(['POST'])
def signup(request):
    username = request.data.get('username')
    if User.objects.filter(username=username).exists():
        return Response({'error': 'ID has already existed.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = UserSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes([AllowAny])
@api_view(['POST'])
def signin(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        login(request, user)
        request.session['user_id'] = user.id
        encoded_jwt = jwt.encode(
            {'username': user.username}, 'SECRET', algorithm='HS256').decode('utf-8')
        response = JsonResponse({"token": str(encoded_jwt)})
        return response

    return JsonResponse({'error': 'User does not exist'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['DELETE'])
def signout(request):
    if request.session['user_id']:
        del(request.session['user_id'])
        return HttpResponse(status=200)
    return HttpResponse(status=401)
