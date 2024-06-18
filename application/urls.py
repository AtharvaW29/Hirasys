from django.urls import path
from . import views

urlpatterns = [
    path('create-application/', views.create_application, name='create-application'),
]
