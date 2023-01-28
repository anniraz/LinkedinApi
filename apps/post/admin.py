from django.contrib import admin

from apps.post.models import Post, PostImage,PostsLike,PostTag



admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(PostsLike)
admin.site.register(PostTag)
