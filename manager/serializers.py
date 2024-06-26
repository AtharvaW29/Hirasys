from rest_framework import serializers
from .models import HRManager
from django.contrib.auth.models import User, Group
from django.contrib.auth.password_validation import validate_password as django_validate_password
from django.core.exceptions import ValidationError as DjangoValidationError

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True}
        }

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists")
        return value
    
    def validate_password(self, value):
        try:
            django_validate_password(value)
        except DjangoValidationError as e:
            raise serializers.ValidationError(str(e))
        if not any(char.isupper() for char in value):
            raise serializers.ValidationError('Password must contain at least one upper case letter')
        return value

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class HRManagerSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()
    username = serializers.CharField(source='user.username')
    email = serializers.EmailField(source='user.email')
    lastname = serializers.CharField(source='user.last_name')
    firstname = serializers.CharField(source='user.first_name')
    password = serializers.CharField(source='user.password', write_only=True, style={'input_type': 'password'})

    class Meta:
        model = HRManager
        fields = ['id', 'username', 'email', 'lastname', 'firstname', 'password', 'company', 'role', 'created_at', 'updated_at', 'profile_pic']
        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserModelSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        role = validated_data['role']

        if role == 'HRAdmin':
            group = Group.objects.get(name='HRAdmin')
        elif role == 'HR':
            group = Group.objects.get(name='HR')
        else:
            group = Group.objects.get(name='HREmp')

        user.groups.add(group)
        user.save()

        hr_manager = HRManager.objects.create(user=user, **validated_data)
        return hr_manager

    def update(self, instance, validated_data):
        user_data = validated_data.get('user', {})
        user = instance.user
        
        user_serializer = UserModelSerializer(user, data=user_data, partial=True)
        user_serializer.is_valid(raise_exception=True)
        user_serializer.save()
        
        instance.company = validated_data.get('company', instance.company)
        instance.role = validated_data.get('role', instance.role)

        instance.user.groups.clear()
        if instance.role == 'HRAdmin':
            group = Group.objects.get(name='HRAdmin')
        elif instance.role == 'HR':
            group = Group.objects.get(name='HR')
        else:
            group = Group.objects.get(name='HREmp')
        
        instance.user.groups.add(group)
        instance.user.save()

        instance.save()
        return instance