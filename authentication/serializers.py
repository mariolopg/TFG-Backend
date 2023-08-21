from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import LoginSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from scraper.serializers import BuildSerializer

User = get_user_model()
class CustomRegistrationSerializer(RegisterSerializer):
  first_name = serializers.CharField()
  last_name = serializers.CharField()

class CustomUserSerializer(serializers.ModelSerializer):
    builds = BuildSerializer(read_only=True, many=True, source='build_set')
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'builds')