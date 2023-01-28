from django.contrib.auth import get_user_model

from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.subscriptions.models import Follower
from apps.subscriptions.serializers import FollowSerializer

User = get_user_model()


class FollowApiView(generics.CreateAPIView):
    queryset = Follower.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        return serializer.save(from_user=self.request.user)


class FollowsApiView(generics.ListAPIView):
    serializer_class = FollowSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        user=User.objects.get(id=pk)
        return Follower.objects.filter(from_user=user)


class FollowersApiView(generics.ListAPIView):
    serializer_class = FollowSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        user=User.objects.get(id=pk)
        return Follower.objects.filter(to_user=user)


class UnfollowApiView(generics.DestroyAPIView):
    serializer_class=FollowSerializer
    queryset = Follower.objects.all()

    def destroy(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        follower = Follower.objects.get(id=pk)
        if follower.from_user == request.user:
            return super().destroy(request, *args, **kwargs)    
        return Response({'error': 'this user is not followed '})


class DeleteFollowerApiView(generics.DestroyAPIView):
    serializer_class=FollowSerializer
    queryset = Follower.objects.all()

    def destroy(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        follower=Follower.objects.get(id=pk)
        print(follower.from_user)
        if follower.to_user==request.user:
            return super().destroy(request, *args, **kwargs)
        return Response({'error':'this user is not your follower'})


