from django.contrib.auth.models import Group, User
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics
from .models import HRManager
from .serializers import HRManagerSerializer
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .permissions import IsHRAdmin, IsHR, IsHREmp


# Create your views here.
@api_view(['GET'])
def sample(request):
    group = Group.objects.get(name='HRAdmin')
    permissions = group.permissions.all()
    for perm in permissions:
        print(perm)
    content_types = ContentType.objects.all()
    for ct in content_types:
        print(ct.app_label, ct.model)
    resp = '{perm}, {ct.app_label}, {ct.model}'
    return Response(resp, status=status.HTTP_200_OK)

class HRManagerListView(generics.ListAPIView):
    queryset = HRManager.objects.all()
    serializer_class = HRManagerSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions, IsHRAdmin | IsHR | IsHREmp]

class HRManagerDetailView(generics.RetrieveAPIView):
    queryset = HRManager.objects.all()
    serializer_class = HRManagerSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions, IsHRAdmin | IsHR | IsHREmp]

class HRManagerCreateView(generics.CreateAPIView):
    queryset = HRManager.objects.all()
    serializer_class = HRManagerSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions]

class HRManagerUpdateView(generics.UpdateAPIView):
    queryset = HRManager.objects.all()
    serializer_class = HRManagerSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions, IsHRAdmin | IsHR]

class HRManagerDeleteView(generics.DestroyAPIView):
    queryset = HRManager.objects.all()
    serializer_class = HRManagerSerializer
    permission_classes = [IsAuthenticated, DjangoModelPermissions, IsHRAdmin]