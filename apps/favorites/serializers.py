from rest_framework import serializers

from apps.favorites.models import Favorite,FavoriteFolder


class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('folder','post','user',)
        read_only_fields = ("id", 'user',)


class FavoriteCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteFolder
        fields = ('id','title','user',)
        read_only_fields = ('user',)