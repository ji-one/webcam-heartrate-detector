from rest_framework import serializers
from heartrate.models import HR

class HRSerializer(serializers.ModelSerializer):
    class Meta:
        model = HR
        fields = ('user', 'bpm', 'created_at')
