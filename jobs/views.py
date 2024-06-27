from rest_framework import status, generics, permissions
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer
from application.models import Application
from application.serializers import ApplicationSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from manager.permissions import IsHRAdmin, IsHR, IsHREmp
# Create your views here.
#POST a Job
class CreateJobViewSet(generics.ListCreateAPIView):
    queryset= Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions, IsHRAdmin | IsHR]

#GET job and their applications
@api_view(['GET'])
@permission_classes([IsAuthenticated, DjangoModelPermissions, IsHRAdmin | IsHR | IsHREmp])
def getJobView(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
    except Job.DoesNotExist:
        return Response({'error': 'No such job with that key'}, status=status.HTTP_404_NOT_FOUND)
    applications = Application.objects.filter(job_id=job_id)

    app_res = ApplicationSerializer(applications, many=True)
    job_res = JobSerializer(job)

    resp = {"job": job_res.data, "application": app_res.data}
    return Response(resp, status=status.HTTP_200_OK)

# DELETE a Job
@api_view(['DELETE'])
@permission_classes([IsAuthenticated, DjangoModelPermissions, IsHRAdmin])
def deleteJobView(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Job.DoesNotExist:
        return Response({'error': 'No such Job with that key'}, status=status.HTTP_404_NOT_FOUND)
    
# UPDATE a Job
@api_view(['PUT'])
@permission_classes([IsAuthenticated, DjangoModelPermissions, IsHRAdmin | IsHR])
def updateJobView(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
    except Job.DoesNotExist:
        return Response({'error': 'No such Job with that key'}, status=status.HTTP_404_NOT_FOUND)
    serializer = JobSerializer(job, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#GET all jobs
@api_view(['GET'])
@permission_classes([IsAuthenticated, DjangoModelPermissions, IsHRAdmin | IsHR | IsHREmp])
def getAllJobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)