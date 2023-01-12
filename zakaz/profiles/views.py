from rest_framework import viewsets
from rest_framework import permissions

from .serializers import ProfileSerializer
from .models import Profile
from .permissions import ProfilePermission


class ProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, ProfilePermission)
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
