from django.db.models import Q

from rest_framework import generics,permissions
from rest_framework.response import Response

from apps.user.serializers import UserSerializer                             
from apps.chat.models import Message,ChatRoom
from apps.chat.serializers import *
from apps.chat.permissions import IsMessageOwner



class  ChatRoomApiView(generics.CreateAPIView):

    '''for creating chats room'''

    queryset=ChatRoom.objects.all()
    serializer_class=ChatRoomSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        return serializer.save(sender=self.request.user)



class  ChatRoomDeleteApiView(generics.DestroyAPIView):

    '''for deleting chats room'''

    queryset=ChatRoom.objects.all()
    serializer_class=ChatRoomSerializer
    permission_classes=[IsMessageOwner]




class SendMessageApiView(generics.ListCreateAPIView):

    '''To send and receive private messages'''

    queryset=Message.objects.all()
    serializer_class=MessageSerializer


    def get(self,request,pk):
        chat_room=ChatRoom.objects.get(id=pk)
        if request.user == chat_room.sender or request.user == chat_room.receiver:
            messages=Message.objects.filter(chat_room=chat_room)
            serializer=MessageSerializer(messages,many=True)
            return Response(serializer.data)
        else:
            return Response({'error':"you don't have this chat"})


    def create(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        chat_room=ChatRoom.objects.get(id=pk)
        if request.user == chat_room.sender or request.user == chat_room.receiver:
            return super().create(request,*args, **kwargs)
        return Response({"ERROR":"You cannot send message it's not your contact"})


    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        receiver=ChatRoom.objects.get(id=pk).receiver
        sender=self.request.user
        if receiver==sender:
            return serializer.save(chat_room=ChatRoom.objects.get(id=pk),receiver=ChatRoom.objects.get(id=pk).sender,sender=sender)
        return serializer.save(chat_room=ChatRoom.objects.get(id=pk),receiver=receiver,sender=sender)



class MessageDetailApiView(generics.RetrieveUpdateDestroyAPIView):

    '''To delete and update messages'''

    queryset=Message.objects.all()
    serializer_class=MessageSerializer
    permission_classes=[IsMessageOwner]



class LIstOfContacts(generics.ListAPIView):

    '''Your all contacts list '''

    queryset=ChatRoom.objects.all()
    serializer_class=ChatRoomSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        return ChatRoom.objects.filter(Q(sender=self.request.user)|Q(receiver=self.request.user))

