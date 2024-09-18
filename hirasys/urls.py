from django.http import HttpResponse
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token


def home_view(request):
    return HttpResponse("Welcome to Hirasys!")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.urls')),
    path('application/', include('application.urls')),
    path('job/', include('jobs.urls')),
    path('manager/', include('manager.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('company/', include('company.urls')),
    path('', home_view),
]
