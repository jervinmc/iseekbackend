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
import time
import requests
import json
from pprint import pprint
import json

class RecommendedItems(generics.GenericAPIView):
    def get(self,request,format=None,longitude='',latitude='',language='en'):
        aps = Nominatim(user_agent="tutorial")
        """This function returns an address as raw from a location
        will repeat until success"""
        # build coordinates string to pass to reverse() functio
        coordinates = f"{latitude}, {longitude}"
        location = aps.reverse(coordinates, language=language).raw
        if(location['address'].get('county')==None):
            data = getRecommended(location['address']['city'])
        else:
            data = getRecommended(location['address']['county'])
        return Response(data=data)

        

def getRecommended(cityName):
    print("nice")
    response= requests.request("GET",f'https://www.trabahanap.com/api/search-new?key=&cityName={cityName}&page=1&compId=')
    listItem = []
    
    x = json.loads(response.text)
    print(x)
    if(len(x['jobs']['rows'])==0):
        pass
    else:
        listData = x['jobs']['rows'][0]
        for i in listData:
            listItem.append({"jobTitle":i['jobTitle'],"image":i['companyLogo'],"jobDescription":i['jobDescription'],"location":i['cityName'],"companyName":i['companyName'],"link":f"https://www.trabahanap.com/search/jobs/details/{i['jobId']}"})
        
    response= requests.request("GET",f'https://search.bossjob.com/api/v1/search/job_filter?company_industries=&degrees=&is_company_verified=0&job_categories=&job_locations={cityName}&job_types=&page=1&query={cityName}&salary_from=&salary_to=&size=18&sort=2&source=web&status=&xp_lvls=')
    x = json.loads(response.text)
    listData = x['data']['jobs']
    for i in listData:
        listItem.append({"jobTitle":i['job_title'],"image":i['company_logo'],"jobDescription":i['job_description'],"location":i['job_location'],"companyName":i['company_name'],"link":f"https://bossjob.ph/job/{i['id']}"})
    
    url = "https://www.philjobnet.gov.ph/jobs/vacant/"
    payload=f'JobLocation={cityName}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'ci_session=f7v0lv211k6i5tjcmj4uqumradbedb6d'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    x = json.loads(response.text)
    
    print("okay")
    print(cityName)
    print(x)
    if(x.get('data')==None):
        pass
    else:
        listData = x['data']
        for i in listData:
            listItem.append({"jobTitle":i['job_title'],"image":"business_logo","jobDescription":i['job_description'],"location":i['job_location'],"companyName":i['business_name'],"link":f"https://www.philjobnet.gov.ph/joboverview/{i['job_code']}"})
    return listItem


class getSearchedJob(generics.GenericAPIView):
    def get(self,request,pk=None,cityName='',searchvalue=''):
        key = ''
        if(cityName=='all'):
            cityName=''
            pass
        if(searchvalue!='all'):
            key = searchvalue
        # print(key)
        response= requests.request("GET",f'https://www.trabahanap.com/api/search-new?key={key}&cityName={cityName}&page=1&compId=')
        listItem = []
        listData=[]
        x = json.loads(response.text)
        if(x.get('jobs')==None):
            listData = x['jobs']['rows'][0]
            for i in listData:
                listItem.append({"jobTitle":i['jobTitle'],"image":i['companyLogo'],"jobDescription":i['jobDescription'],"location":i['cityName'],"companyName":i['companyName'],"link":f"https://www.trabahanap.com/search/jobs/details/{i['jobId']}"})
            
        response= requests.request("GET",f'https://search.bossjob.com/api/v1/search/job_filter?company_industries={key}&degrees=&is_company_verified=0&job_categories=&job_locations={cityName}&job_types=&page=1&query={cityName}&salary_from=&salary_to=&size=18&sort=2&source=web&status=&xp_lvls=')
        x = json.loads(response.text)
        print(x)
        listData = x['data']['jobs']
        for i in listData:
            listItem.append({"jobTitle":i['job_title'],"image":i['company_logo'],"jobDescription":i['job_description'],"location":i['job_location'],"companyName":i['company_name'],"link":f"https://bossjob.ph/job/{i['id']}"})
        
        url = "https://www.philjobnet.gov.ph/jobs/vacant/"
        payload=f'JobLocation={cityName}&JobSearch={key}'
        headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': 'ci_session=f7v0lv211k6i5tjcmj4uqumradbedb6d'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        x = json.loads(response.text)
        data_validation = x['data']
        print(data_validation)
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
                listItem.append({"jobTitle":i['job_title'],"image":"business_logo","jobDescription":i['job_description'],"location":i['job_location'],"companyName":i['business_name'],"link":f"https://www.philjobnet.gov.ph/joboverview/{i['job_code']}"})
        return Response(data = listItem)





class Inquire(generics.GenericAPIView):
    def post(self,request,format=None):
        message = get_template('inquiry.html').render({"email":request.data.get('email'),"message":request.data.get('message'),"name":request.data.get('name')})
        msg = EmailMultiAlternatives('Inquiry', message,'iseekwebapp@gmail.com', ['iseekwebapp.contactus@gmail.com'])
        html_content = '<p>This is an <strong>important</strong> message.</p>'
        msg.content_subtype = "html"
        msg.send()
        return Response(status=status.HTTP_200_OK)
