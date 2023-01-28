from django.contrib import admin

from apps.favorites.models import Favorite,FavoriteFolder

# Register your models here.
admin.site.register(Favorite)
admin.site.register(FavoriteFolder)