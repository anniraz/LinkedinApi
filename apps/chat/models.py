from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()


class ChatRoom(models.Model):
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    sender= models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')        
    is_contact = models.BooleanField(default=False)

    
    def __str__(self):
           return f'reciever:{self.receiver} sender:{self.sender}'
      
    class Meta:
        unique_together=(('receiver','sender',),)



class Message(models.Model):
    chat_room=models.ForeignKey(ChatRoom,on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_message')
    sender= models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_message')        
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'message:{self.message}'

    class Meta:
       ordering = ('timestamp',)