from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from heartrate.models import HR
from accounts.models import User

# Create your views here.
@api_view(['POST'])
def save_bpm(request):
    if not request.session.get('user_id'):
        return HttpResponse(status=401)
    
    user_id = request.session.get('user_id')
    user = User.objects.get(pk = user_id)
    hr = HR(user = user, bpm = request.data.get('bpm'))
    hr.save()
    return HttpResponse(status=201)
