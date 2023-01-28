from django.contrib import admin

from apps.comments.models import Comment,CommentLike

admin.site.register(Comment)
admin.site.register(CommentLike)