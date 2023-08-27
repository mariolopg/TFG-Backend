import json
from rest_framework.views import APIView
from rest_framework import status, viewsets
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView
from dj_rest_auth.serializers import TokenSerializer, UserDetailsSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from .permissions import ReadOnly
from .serializers import CustomUserSerializer, CustomRegistrationSerializer
from scraper.models import Build, Comment

User = get_user_model()
class CustomRegistrationView(RegisterView):
  serializer_class = CustomRegistrationSerializer

class CustomLoginView(LoginView):
  def get_response(self):
    serializer = TokenSerializer(instance=self.token, context={'request': self.request})
    user = self.user
    user_data = UserDetailsSerializer(user).data
    user_data['is_admin'] = user.is_staff
    user_data['date_joined'] = user.date_joined

    response = {
        'token': serializer.data.get('key'),
        'user': user_data
    }

    return Response(response, status=status.HTTP_200_OK)

class DeactivateAccount(APIView):
  permission_classes = [IsAuthenticated]

  def delete(self, request, *args, **kwargs):
    user = self.request.user
    user.is_active = False
    user.save()

    Build.objects.filter(builder=user).delete()
    Comment.objects.filter(builder=user).delete()

    return Response({"data": _("User was succesfully deactivated.")}, status=status.HTTP_200_OK)
    
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.filter(is_active=True)
  serializer_class = CustomUserSerializer
  permission_classes = [ReadOnly]