from django.urls import path
from . import views

urlpatterns = [
    path('applications/', views.CreateApplicationViewSet.as_view(), name='application-list-create'),
    path('applications/', views.getApplicationView, name='application-list'),
    path('applications/<int:application_id>/', views.updateApplicationView, name='application-update'),
    path('applications/<int:application_id>/delete/', views.deleteApplicationView, name='application-delete'),
]
