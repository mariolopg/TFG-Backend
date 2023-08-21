from rest_framework.views import APIView
from rest_framework import status, viewsets
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView
from dj_rest_auth.serializers import TokenSerializer, UserDetailsSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .permissions import ReadOnly
from .serializers import CustomUserSerializer, CustomRegistrationSerializer

User = get_user_model()
class CustomRegistrationView(RegisterView):
  serializer_class = CustomRegistrationSerializer

class CustomLoginView(LoginView):
  def get_response(self):
    serializer = TokenSerializer(instance=self.token, context={'request': self.request})
    user = self.user
    user_serializer = UserDetailsSerializer(user)

    response = {
        'token': serializer.data.get('key'),
        'user': user_serializer.data
    }

    return Response(response, status=status.HTTP_200_OK)

class DeactivateAccount(APIView):
  permission_classes = [IsAuthenticated]

  def delete(self, request, *args, **kwargs):
    user = self.request.user
    user.is_active = False
    user.save()
    return Response({"data": "user deactivated"}, status=status.HTTP_200_OK)
    
class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.filter(is_active=True)
  serializer_class = CustomUserSerializer
  permission_classes = [ReadOnly]