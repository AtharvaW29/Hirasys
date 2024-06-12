from rest_framework import serializers
from .models.candidate import Candidate

class ApplicationSerializer(serializers.Serializer):
    job_title = serializers.CharField(max_length=255)
    company_name = serializers.CharField(max_length=255)
    date_applied = serializers.DateField(format="%Y-%m-%d", input_formats=["%Y-%m-%d", "iso-8601"])

class SkillsSerializer(serializers.Serializer):
    skill = serializers.CharField(max_length=100)

class CandidateSerializer(serializers.ModelSerializer):
    applications = ApplicationSerializer(many=True)
    skills = SkillsSerializer(many=True)

    class Meta:
        model = Candidate
        fields = '__all__'

    def create(self, validated_data):
        applications_data = validated_data.pop('applications')
        skills_data = validated_data.pop('skills')
        
        # Convert date objects to strings
        for application in applications_data:
            application['date_applied'] = application['date_applied'].strftime('%Y-%m-%d')
        
        # Directly creating candidate instance
        candidate = Candidate.objects.create(**validated_data)
        
        # Append applications to candidate.applications
        candidate.applications = applications_data
        
        # Append skills to candidate.skills
        candidate.skills = skills_data
        
        # Save candidate with embedded documents
        candidate.save()
        
        return candidate
