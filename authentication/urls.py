# authentication/urls.py
from rest_framework import routers
from django.urls import path, include
from dj_rest_auth.views import LogoutView, UserDetailsView
from .views import CustomRegistrationView, DeactivateAccount, UserViewSet, CustomLoginView

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path("register/", CustomRegistrationView.as_view(), name="rest_register"),
    path("login/", CustomLoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    # path("user/", UserDetailsView.as_view(), name="rest_user_details"),
    path("deactivate/", DeactivateAccount.as_view(), name="rest_user_deactivate"),
    path("", include(router.urls)),
]