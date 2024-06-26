from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, generics



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