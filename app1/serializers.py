from . import models
from rest_framework import serializers

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.state
        fields = ['id', 'state_Name',  'city_Name','tenderOrder']

        # ,'status', 'created_on'