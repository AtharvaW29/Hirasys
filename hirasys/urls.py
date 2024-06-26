from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('base.urls')),
    path('application/', include('application.urls')),
    path('job/', include('jobs.urls')),
    path('manager/', include('manager.urls'))
]
