from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegistrationSerializer

class CustomRegistrationView(RegisterView):
  serializer_class = CustomRegistrationSerializer