from django.shortcuts import render
from rest_framework import viewsets,generics,status
from .models import User
from .serializers import UserSerializer
from rest_framework import filters
from rest_framework.response import Response
class UserView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=User.objects.all()
    serializer_class=UserSerializer


class Login(generics.GenericAPIView):
    def post(self,request,format=None):
        try:
            res = request.data
            items = User.objects.filter(email=res.get('email'),password=res.get('password')).count()
            if(items>0):
               items = User.objects.filter(email=res.get('email'),password=res.get('password')) 
               items = UserSerializer(items,many=True)
               return Response(status=status.HTTP_200_OK,data=items.data)
            return Response(status=status.HTTP_200_OK,data="no_data")
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])