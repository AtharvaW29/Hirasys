from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from company.models import Company
from manager.models import HRManager
from company.serializers import CompanySerializer
from django.db import transaction
from rest_framework.permissions import AllowAny

class RegisterView(APIView):
    permission_classes = [AllowAny]

    @transaction.atomic
    def post(self, request):
        # User creation
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')

        if not username or not password or not email:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)

        # Company creation
        company_data = request.data.get('company')
        company_serializer = CompanySerializer(data=company_data)
        
        if company_serializer.is_valid():
            company = company_serializer.save()  # Ensure company is saved before proceeding
            print(f"Company instance: {company}, Company ID: {company.id}")
            
            if company and company.id:  # Ensure company instance is created and valid
                # Assign user as HR Admin using the company instance
                HRManager.objects.create(user=user, company=company, role='HRAdmin')

                # Generate auth token
                token = Token.objects.create(user=user)
                
                return Response({
                    'message': 'Registration successful',
                    'token': token.key,
                    'company': company_serializer.data,
                }, status=status.HTTP_201_CREATED)

            return Response({'error': 'Failed to create company'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
