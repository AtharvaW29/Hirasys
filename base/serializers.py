from rest_framework import serializers
from .models.candidate import Candidate, Education, Experience, Skill, Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    education = EducationSerializer()
    experiences = ExperienceSerializer(many=True)
    skills = SkillSerializer(many=True)
    applications = ApplicationSerializer(many=True)

    class Meta:
        model = Candidate
        fields = '__all__'