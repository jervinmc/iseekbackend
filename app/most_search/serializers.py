from rest_framework import serializers
from .models import MostSearch

class MostSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model=MostSearch
        fields="__all__"
