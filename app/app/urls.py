from django.contrib import admin
from django.conf import settings
from django.urls import path
from django.urls.conf import include
from api.views import RecommendedItems,getSearchedJob,Inquire,MostSearchAPI,HighestPaidJobs

from most_demand.views import MostDemandAPI
from users.views import Login

urlpatterns = [
    path('api/v1/admin/', admin.site.urls),
    path('api/v1/getdata/<str:latitude>/<str:longitude>', RecommendedItems.as_view(), name='Sign up'),
    path('api/v1/search/<str:cityName>/<str:searchvalue>/<str:salaryFrom>/<str:salaryTo>/', getSearchedJob.as_view(), name='Sign up'),
    path('api/v1/inquire', Inquire.as_view(), name='Sign up'),
    path('api/v1/mostsearch/', include('most_search.urls')),
    path('api/v1/login/', Login.as_view(), name='get_user'),
    path('api/v1/demand/', include('most_demand.urls')),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/mostdemanddata/', MostDemandAPI.as_view(), name='Sign up'),
    path('api/v1/mostsearchdata/', MostSearchAPI.as_view(), name='Sign up'),
    path('api/v1/highestpaidjob/', HighestPaidJobs.as_view(), name='Sign up'),
    
    
    
]

