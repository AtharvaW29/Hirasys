from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models.candidate import Candidate
from .serializers import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')
