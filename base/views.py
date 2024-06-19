from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from .candidate import Candidate
from .serializers import CandidateSerializer
from application.models import Application
from application.serializers import ApplicationSerializer
from rest_framework.decorators import api_view,authentication_classes, permission_classes
from django.contrib.auth.models import User

class CreateApplicationViewSet(generics.ListCreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


# GET candidate and their application details
@api_view(['GET'])
def getCandidateView(request, candidate_id):
    try:
        candidate = Candidate.objects.get(pk=candidate_id)
    except Candidate.DoesNotExist:
        return Response({'error': 'No such Candidate with that primary key'}, status=status.HTTP_404_NOT_FOUND)
    
    applications = Application.objects.filter(candidate_id=candidate_id)
    print(f"Applications for candidate {candidate_id}: {applications}") 
    app_res = ApplicationSerializer(applications, many=True)
    cand_res = CandidateSerializer(candidate)

    print(f"Serialized applications: {app_res.data}") 
    resp = {"candidate": cand_res.data, "applications": app_res.data}
    
    return Response(resp, status=status.HTTP_200_OK)

#POST candidate details
@api_view(['POST'])
def postCandidateView(request):
    try:
        candidate_data = request.data.get('candidate')
        
        candidate_serializer = CandidateSerializer(data=candidate_data)
        if candidate_serializer.is_valid():
            candidate = candidate_serializer.save()
        else:
            return Response(candidate_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        response_data = {"candidate": CandidateSerializer(candidate).data}
        return Response(response_data, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
#DELETE a Candidate
# views.py
@api_view(['DELETE'])
def deleteCandidateView(request, candidate_id):
    try:
        candidate = Candidate.objects.get(pk=candidate_id)
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Candidate.DoesNotExist:
        return Response({'error': 'No such Candidate with that primary key'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def updateCandidateView(request, candidate_id):
    try:
        candidate = Candidate.objects.get(pk=candidate_id)
    except Candidate.DoesNotExist:
        return Response({'error': 'No such Candidate with that primary key'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = CandidateSerializer(candidate, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')
