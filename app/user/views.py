"""
Views for the user api

"""

from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSeralizer
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the systen"""
    serializer_class = UserSerializer

class CreateTokenView(ObtainAuthToken):
    """Create a new Auth token for user."""
    serializer_class = AuthTokenSeralizer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user - PATCH Request"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user - GET Request"""
        return self.request.user






