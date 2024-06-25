from django.urls import path
from . import views

urlpatterns = [
    path('applications/', views.CreateApplicationViewSet.as_view(), name="list-create-applications"),
    path('get-applications/', views.getApplicationView, name="get-applications"),
    path('update-application/<int:application_id>/', views.updateApplicationView, name="update-applications"),
    path('delete-application/<int:application_id>/', views.deleteApplicationView, name="delete-application"),
]