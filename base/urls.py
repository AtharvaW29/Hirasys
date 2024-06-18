from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('room/', views.room, name="room"),
    path('candidate/', views.CreateApplicationViewSet.as_view(), name='create-candidate'),
    path('candidate/<int:candidate_id>/', views.getCandidateView, name="get-candidate"),
    path('candidate/delete/<int:candidate_id>/', views.deleteCandidateView, name='delete-candidate'),
    path('candidate/update/<int:candidate_id>/', views.updateCandidateView, name='update-candidate')
]
