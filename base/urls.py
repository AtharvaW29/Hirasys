from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CandidateModelViewSet
from . import views

router = DefaultRouter()
# router.register(r'testmodel', TestModelViewSet)
router.register(r'candidate', CandidateModelViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Include router URLs here
    path('home/', views.home, name="home"),
    path('room/', views.room, name="room"),
]
