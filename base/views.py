from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models.candidate import Candidate
from .serializers import CandidateSerializer, EducationSerializer, ExperienceSerializer, SkillSerializer, ApplicationSerializer

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def create(self, request, *args, **kwargs):
        email = request.data.get('email')
        if Candidate.objects.filter(email=email).exists():
            return Response({"detail": "A candidate with this email already exists."}, status=status.HTTP_400_BAD_REQUEST)

        education_data = request.data.pop('education')
        education_serializer = EducationSerializer(data=education_data)
        education_serializer.is_valid(raise_exception=True)
        education = education_serializer.save()

        experience_data = request.data.pop('experiences')
        experiences = []
        for exp_data in experience_data:
            exp_serializer = ExperienceSerializer(data=exp_data)
            exp_serializer.is_valid(raise_exception=True)
            experience = exp_serializer.save()
            experiences.append(experience)

        skill_data = request.data.pop('skills')
        skills = []
        for skill in skill_data:
            skill_serializer = SkillSerializer(data=skill)
            skill_serializer.is_valid(raise_exception=True)
            skill_obj = skill_serializer.save()
            skills.append(skill_obj)

        application_data = request.data.pop('applications')
        applications = []
        for app_data in application_data:
            app_serializer = ApplicationSerializer(data=app_data)
            app_serializer.is_valid(raise_exception=True)
            application = app_serializer.save()
            applications.append(application)

        candidate = Candidate(
            name=request.data.get('name'),
            email=email,
            phone=request.data.get('phone'),
            education=education
        )
        candidate.save()
        candidate.experiences.set(experiences)
        candidate.skills.set(skills)
        candidate.applications.set(applications)

        return Response(CandidateSerializer(candidate).data, status=status.HTTP_201_CREATED)

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')
