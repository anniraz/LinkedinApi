from django.db import models
from django.contrib.auth import get_user_model
from apps.post.models import Post

User=get_user_model()

class FavoriteFolder(models.Model):
    title=models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='favorite_folder_user', on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.title} {self.user.username}'

class Favorite(models.Model):
    folder=models.ForeignKey(FavoriteFolder,on_delete=models.CASCADE,null=True,blank=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE ,related_name='post')
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post.title}'

    class Meta:
        unique_together = (('post', 'user',),)