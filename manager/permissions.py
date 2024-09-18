from rest_framework.permissions import BasePermission

class IsHRAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.hrmanager.role == 'HRAdmin'

class IsHR(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.hrmanager.role == 'HR'

class IsHREmp(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.hrmanager.role == 'Employee'
