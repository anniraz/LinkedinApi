from rest_framework import viewsets,filters
from rest_framework.response import Response
# from django_filters.rest_framework import DjangoFilterBackend

from apps.favorites.models import Favorite,FavoriteFolder
from apps.favorites.serializers import FavoriteSerializer,FavoriteCategorySerializer
from apps.user.permissions import IsOwner



class FavoriteCategoryApiViewSet(viewsets.ModelViewSet):
    # your own category(favorite) 

    queryset=FavoriteFolder.objects.all()
    serializer_class=FavoriteCategorySerializer
    # filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    # filterset_fields = ['title']
    permission_classes=(IsOwner,)


    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def list(self, request):
        # queryset=self.filter_queryset(self.get_queryset()).filter(user=request.user)
        queryset=FavoriteFolder.objects.filter(user=request.user)
        serializer = FavoriteCategorySerializer(queryset, many=True)
        return Response(serializer.data)




class FavoriteApiViewSet(viewsets.ModelViewSet):
    # your own favorites

    queryset=Favorite.objects.all()
    serializer_class=FavoriteSerializer
    # filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    # filterset_fields = ['folder','post']
    permission_classes=[IsOwner]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def list(self, request):
        # queryset=self.filter_queryset(self.get_queryset()).filter(user=request.user)
        queryset=Favorite.objects.filter(user=request.user)
        serializer = FavoriteSerializer(queryset, many=True)
        return Response(serializer.data)