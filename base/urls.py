from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('candidates/', views.CreateApplicationViewSet.as_view(), name='list-create-candidates'),  # For list and create
    path('candidate/<int:candidate_id>/', views.getCandidateView, name="get-candidate"),  # For retrieving a specific candidate
    path('candidate/delete/<int:candidate_id>/', views.deleteCandidateView, name='delete-candidate'),  # For deleting a specific candidate
    path('candidate/update/<int:candidate_id>/', views.updateCandidateView, name='update-candidate')  # For updating a specific candidate
]
