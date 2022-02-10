from django.shortcuts import render
from rest_framework import viewsets,generics,status
from .models import MostSearch
from .serializers import MostSearchSerializer
from rest_framework import filters
from django.db.models import F
from rest_framework.response import Response
class MostSearchView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=MostSearch.objects.all()
    serializer_class=MostSearchSerializer
    def create(self,request):
        res = request.data
        items = MostSearch.objects.filter(search_location=res.get('search_location'),search_job=res.get('search_job')).count()
        if(items>0):
            items = MostSearch.objects.filter(search_location=res.get('search_location'),search_job=res.get('search_job')).update(quantity=F('quantity')+1)
            print('already have')
        else:
            items = MostSearchSerializer(data=res)
            items.is_valid(raise_exception=True)
            items.save()
        return Response(status=status.HTTP_200_OK)
