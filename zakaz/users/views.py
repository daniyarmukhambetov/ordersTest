from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, UserLoginSerializer


class UserViewSet(
    viewsets.mixins.CreateModelMixin,
    viewsets.GenericViewSet
):
    def get_serializer_class(self):
        if self.action == 'login':
            return UserLoginSerializer
        return UserSerializer

    def get_permissions(self):
        if self.action == 'ping':
            self.permission_classes = (permissions.IsAuthenticated, )
        return super(UserViewSet, self).get_permissions()

    @action(methods=["post"], detail=False)
    def login(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

    @action(methods=["get"], detail=False)
    def ping(self, request):
        print(request.user)
        return Response({"pong": True}, status=200)
