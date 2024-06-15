from rest_framework import serializers
from .models.candidate import Candidate, Education, Experience, Skill, Application

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class CandidateSerializer(serializers.ModelSerializer):
    education = EducationSerializer()
    experiences = ExperienceSerializer(many=True)
    skills = SkillSerializer(many=True)
    applications = ApplicationSerializer(many=True)

    class Meta:
        model = Candidate
        fields = '__all__'

    def create(self, validated_data):
        education_data = validated_data.pop('education')
        experiences_data = validated_data.pop('experiences')
        skills_data = validated_data.pop('skills')
        applications_data = validated_data.pop('applications')

        education = Education.objects.create(**education_data)
        candidate = Candidate.objects.create(education=education, **validated_data)

        for exp_data in experiences_data:
            experience = Experience.objects.create(**exp_data)
            candidate.experiences.add(experience)

        for skill_data in skills_data:
            skill = Skill.objects.create(**skill_data)
            candidate.skills.add(skill)

        for app_data in applications_data:
            application = Application.objects.create(**app_data)
            candidate.applications.add(application)

        return candidate

    def update(self, instance, validated_data):
        education_data = validated_data.pop('education', None)
        experiences_data = validated_data.pop('experiences', None)
        skills_data = validated_data.pop('skills', None)
        applications_data = validated_data.pop('applications', None)

        if education_data:
            Education.objects.filter(id=instance.education.id).update(**education_data)

        if experiences_data:
            instance.experiences.clear()
            for exp_data in experiences_data:
                experience = Experience.objects.create(**exp_data)
                instance.experiences.add(experience)

        if skills_data:
            instance.skills.clear()
            for skill_data in skills_data:
                skill = Skill.objects.create(**skill_data)
                instance.skills.add(skill)

        if applications_data:
            instance.applications.clear()
            for app_data in applications_data:
                application = Application.objects.create(**app_data)
                instance.applications.add(application)

        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.save()

        return instance
