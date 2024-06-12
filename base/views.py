from django.shortcuts import render
from rest_framework import viewsets
from .models.candidate import Candidate
from .serializers import CandidateSerializer

# class TestModelViewSet(viewsets.ModelViewSet):
#     queryset = TestModel.objects.all()
#     serializer_class = TestModelSerializer

class CandidateModelViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')
