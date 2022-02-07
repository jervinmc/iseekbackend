from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from api.views import RecommendedItems,getSearchedJob,Inquire


urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/getdata/<str:latitude>/<str:longitude>', RecommendedItems.as_view(), name='Sign up'),
    path('api/v1/search/<str:cityName>/<str:searchvalue>', getSearchedJob.as_view(), name='Sign up'),
    path('api/v1/inquire', Inquire.as_view(), name='Sign up'),
]

