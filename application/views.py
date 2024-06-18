from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Application
from .serializers import ApplicationSerializer
# Create your views here.
# Cretae an application
@api_view(['POST'])
def create_application(request):
    if request.method == 'POST':
        serialzer = ApplicationSerializer(data=request.data)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data, status = status.HTTP_201_CREATED)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)