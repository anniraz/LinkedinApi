from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins, permissions,filters

from apps.user.models import *
from apps.user.serializers import *
from apps.user.permissions import IsOwner,IsOwn


class UsersApiView(GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
                   
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['email','first_name','phone_number']


    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwn(),)
        return (permissions.AllowAny(),)



class PositionApiView(GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):

    queryset=Position.objects.all()
    serializer_class=PositionSerializers


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(),)
        return (permissions.AllowAny(),)




class SkillsApiView(GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
                    
    queryset=Skills.objects.all()
    serializer_class=SkillsSerializers

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)


    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(),)
        return (permissions.AllowAny(),)



class EducationInformationApiView(GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
                    
    queryset=EducationInformation.objects.all()
    serializer_class=EducationInformationSerializers


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(),)
        return (permissions.AllowAny(),)





class PremiumViewSet(GenericViewSet,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin):

    queryset=User.objects.all()
    serializer_class=IsPremiumSerializer
    permission_classes=[IsOwn]

    def perform_update(self, serializer):
        if serializer.validated_data['is_premium'] == True:
            return serializer.save(premium_date=timezone.now())
        else:
            return serializer.save(premium_date=None)