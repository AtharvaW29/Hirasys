from rest_framework.permissions import BasePermission

class IsHRAdmin(BaseException):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='HRAdmin').exists()
    
class IsHR(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='HR').exists()

class IsHREmp(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='HREmp').exists()