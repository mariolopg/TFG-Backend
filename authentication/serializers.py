from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from scraper.serializers import BuildSerializer

User = get_user_model()
class CustomRegistrationSerializer(RegisterSerializer):
  first_name = serializers.CharField()
  last_name = serializers.CharField()

  def custom_signup(self, request, user):
    user.first_name = self.validated_data.get('first_name')
    user.last_name = self.validated_data.get('last_name')
    user.save()

class CustomUserSerializer(serializers.ModelSerializer):
    builds = BuildSerializer(read_only=True, many=True, source='build_set')
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'builds')