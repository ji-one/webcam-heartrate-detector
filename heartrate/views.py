from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import HttpResponse
from heartrate.models import AverageHR, HR
from accounts.models import User
from django.db.models import Avg

# Create your views here.


@api_view(['POST'])
def save_bpm(request):
    if not request.session.get('user_id'):
        return HttpResponse(status=401)

    user_id = request.session.get('user_id')
    user = User.objects.get(pk=user_id)
    hr = HR(user=user, bpm=request.data.get('bpm'))
    hr.save()
    average(hr)
    return HttpResponse(status=201)


def average(self, force_insert=False, force_update=False, *args, **kwargs):
    super(HR, self).save(force_insert, force_update, *args, **kwargs)
    if self.user:
        avg_bpm = HR.objects.filter(
            user=self.user, created_at__hour=self.created_at.hour).aggregate(Avg('bpm'))['bpm__avg']
        avg_bpm = round(avg_bpm)

        exist = AverageHR.objects.filter(
            hour=self.created_at.hour, user=self.user)
        if exist:
            exist.update(avg_bpm=avg_bpm)
        else:
            AverageHR.objects.create(
                hour=self.created_at.hour, user=self.user, avg_bpm=avg_bpm)
