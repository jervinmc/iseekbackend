from django.shortcuts import render
from rest_framework import viewsets,generics,status
from .models import MostDemand
from .serializers import MostDemandSerializer
from rest_framework import filters
from django.db.models import F
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import viewsets,generics
from rest_framework import filters
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status, viewsets
import requests
from geopy.geocoders import Nominatim
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from most_search.models import MostSearch
from users.models import User
from most_search.serializers import MostSearchSerializer
import time
import requests
import json
from pprint import pprint
import json
class MostDemandView(viewsets.ModelViewSet):
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=MostDemand.objects.all()
    serializer_class=MostDemandSerializer
    def create(self,request):
        res = request.data
        items = MostDemand.objects.filter(category=res.get('category')).count()
        if(items>0):
            items = MostDemand.objects.filter(category=res.get('category')).update(quantity=F('quantity')+1)
            print('already have')
        else:
            items = MostDemandSerializer(data=res)
            items.is_valid(raise_exception=True)
            items.save()
        return Response(status=status.HTTP_200_OK)


class MostDemandAPI(generics.GenericAPIView):
    def get(self,request,pk=None,cityName=''):
        items = MostDemand.objects.all().order_by('-quantity')[0]
        items = MostDemandSerializer(items)
        print(items.data)
        # print(items.data)
        
        key = ''
        key = items.data['category']
        if(cityName=='all'):
            cityName=''
            pass
        # if(searchvalue!='all'):
        #     key = searchvalue
        # print(key)
        response= requests.request("GET",f'https://www.trabahanap.com/api/search-new?key={key}&cityName={cityName}&page=1&compId=')
        listItem = []
        listData=[]
        x = json.loads(response.text)
        if(x.get('jobs')==None):
            listData = x['jobs']['rows'][0]
            for i in listData:
                listItem.append({"jobTitle":i['jobTitle'],"image":i['companyLogo'],"jobDescription":i['jobDescription'],"location":i['cityName'],"companyName":i['companyName'],"link":f"https://www.trabahanap.com/search/jobs/details/{i['jobId']}","category":i['industryType']})
            
        response= requests.request("GET",f'https://search.bossjob.com/api/v1/search/job_filter?company_industries={key}&degrees=&is_company_verified=0&job_categories=&job_locations={cityName}&job_types=&page=1&query={cityName}&salary_from=&salary_to=&size=18&sort=2&source=web&status=&xp_lvls=')
        x = json.loads(response.text)
        listData = x['data']['jobs']
        for i in listData:
            listItem.append({"jobTitle":i['job_title'],"image":i['company_logo'],"jobDescription":i['job_description'],"location":i['job_location'],"companyName":i['company_name'],"link":f"https://bossjob.ph/job/{i['id']}","category":i['company_industry']})
        
        url = "https://www.philjobnet.gov.ph/jobs/vacant/"
        payload=f'JobLocation={cityName}&JobSearch={key}'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'ci_session=f7v0lv211k6i5tjcmj4uqumradbedb6d'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        x = json.loads(response.text)
        data_validation = x['data']
        # if(len(data_validation)!=0):
        #     pass
        if(data_validation[0].get('Job Search')!=None):
            pass
        # if(x.get('data')==None):
        #     print('okay')
        #     pass
        else:
            listData = x['data']
            for i in listData:
                listItem.append({"jobTitle":i['job_title'],"image":"business_logo","jobDescription":i['job_description'],"location":i['job_location'],"companyName":i['business_name'],"link":f"https://www.philjobnet.gov.ph/joboverview/{i['job_code']}","category":i['keyword']})
        return Response(data = listItem)
