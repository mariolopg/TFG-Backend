from rest_framework import permissions
from django.contrib.auth import get_user_model
from scraper.models import Build, BuildImage

User = get_user_model()
class ReadOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    return request.method in permissions.SAFE_METHODS
  
class IsAuthenticatedCreateOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method in ['POST']:
      builder = User.objects.get(id=request.data['builder'])
      return request.user.is_authenticated and request.user == builder
    
    return True 

class IsOwnerOrReadOnly(permissions.BasePermission):
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True
    
    build = Build.objects.get(id=view.kwargs['pk'])
    return (request.user.is_authenticated and build.builder == request.user) or request.user.is_staff
  
class IsBuildOwnerOrReadOnly(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method in permissions.SAFE_METHODS:
      return True
    
    if request.method in ['POST']:
      build = Build.objects.get(id=request.data['build'])
      return (request.user.is_authenticated and build.builder == request.user) or request.user.is_staff
    
    return request.user.is_authenticated
    
  def has_object_permission(self, request, view, obj):
    if request.method in permissions.SAFE_METHODS:
      return True

    build = BuildImage.objects.get(id=view.kwargs['pk']).build
    return (request.user.is_authenticated and build.builder == request.user) or request.user.is_staff


