from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Application
from .serializers import ApplicationSerializer
# Create your views here.
# Cretae an application
class CreateApplicationViewSet(generics.ListCreateAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

#GET all applications
@api_view(['GET'])
def getApplicationView(request):
    applications = Application.objects.all()
    serializer = ApplicationSerializer(applications, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

#UPDATE application
@api_view(['PUT'])
def updateApplicationView(request, application_id):
    try:
        application = Application.objects.get(pk=application_id)
    except Application.DoesNotExist():
        return Response({'error': 'No such application with that key'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ApplicationSerializer(application, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#DELETE an application
@api_view(['DELETE'])
def deleteApplicationView(request, application_id):
    try:
        application = Application.objects.get(pk=application_id)
        application.delete()
        return Response({'Successfully deleted the application'}, status=status.HTTP_204_NO_CONTENT)
    except Application.DoesNotExist:
        return Response({'error': 'No such application with that key'})