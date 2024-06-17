from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .candidate import Candidate
from .serializers import CandidateSerializer


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    # def create(self, validated_data):
    #     applications_data = validated_data.pop('applications')

    #     candidate = Candidate.objects.create(**validated_data)

    #     for app_data in applications_data:
    #         application = Application.objects.create(**app_data)
    #         candidate.applications.add(application)

    #     return candidate

    # def update(self, instance, validated_data):
    #     applications_data = validated_data.pop('applications', None)

    #     if applications_data:
    #         instance.applications.clear()
    #         for app_data in applications_data:
    #             application = Application.objects.create(**app_data)
    #             instance.applications.add(application)

    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.phone = validated_data.get('phone', instance.phone)
    #     instance.save()

    #     return instance

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')
