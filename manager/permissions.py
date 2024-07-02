from rest_framework.permissions import BasePermission

class IsHRAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='HRAdmin').exists()

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

class IsHR(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='HR').exists()

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)

class IsHREmp(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='HREmp').exists()

    def has_object_permission(self, request, view, obj):
        return self.has_permission(request, view)
