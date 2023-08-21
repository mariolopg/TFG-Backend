from rest_framework import permissions

class ReadOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    return request.method in permissions.SAFE_METHODS

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True 
    
    return request.user.is_authenticated and obj.builder == request.user
  
class IsBuildOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True 
    
    return request.user.is_authenticated and obj.build.builder == request.user

class IsAuthenticatedCreateOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method in ['POST']:
      return request.user.is_authenticated
    
    return True 
