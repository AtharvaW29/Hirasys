from rest_framework import serializers
from .candidate import Candidate


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'

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
