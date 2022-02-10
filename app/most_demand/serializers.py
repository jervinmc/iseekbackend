from rest_framework import serializers
from .models import MostDemand

class MostDemandSerializer(serializers.ModelSerializer):
    class Meta:
        model=MostDemand
        fields="__all__"
