from rest_framework import viewsets,permissions

from apps.comments.serializers import CommentSerializer,CommentLikeSerializer
from apps.comments.models import Comment,CommentLike
from apps.user.permissions import IsOwner


class CommentApiViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(), )
        else:
            return (permissions.IsAuthenticated(),)



class CommentLikeApiView(viewsets.ModelViewSet):

    queryset=CommentLike.objects.all()
    serializer_class=CommentLikeSerializer
    

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            return (IsOwner(), )
        else:
            return (permissions.IsAuthenticated(),)


    def create(self, request, *args, **kwargs):

        comment = request.data['comment']
        user=request.user       
        if  CommentLike.objects.filter(comment_id=comment,user=user):
            return Response({"error":"you can't like twice"})
        return super().create(request,*args, **kwargs)



    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)