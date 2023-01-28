from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions

from apps.user.models import *
from apps.user.serializers import *
from apps.user.permissions import IsOwner



class UsersApiView(GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
                   
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(),)
        return (permissions.AllowAny(),)
