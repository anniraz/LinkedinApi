from rest_framework import serializers

from apps.chat.models import Message,ChatRoom

class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = ['id','receiver','sender',]
        read_only_fields = ('sender',)


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
        read_only_fields = ('id','timestamp','chat_room','sender','receiver',)

