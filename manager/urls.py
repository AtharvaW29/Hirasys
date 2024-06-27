from django.urls import path
from . import views

urlpatterns=[
    path('test/', views.sample, name="sample"),
    path('hr-managers/', views.HRManagerListView.as_view(), name='hr-manager-list'),
    path('hr-managers/<int:pk>/', views.HRManagerDetailView.as_view(), name='hr-manager-detail'),
    path('hr-managers/create/', views.HRManagerCreateView.as_view(), name='hr-manager-create'),
    path('hr-managers/update/<int:pk>/', views.HRManagerUpdateView.as_view(), name='hr-manager-update'),
    path('hr-managers/delete/<int:pk>/', views.HRManagerDeleteView.as_view(), name='hr-manager-delete')
]