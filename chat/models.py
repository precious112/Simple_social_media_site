from django.db import models
from friends.models import FriendList
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Chat(models.Model):
    messengers= models.ForeignKey(FriendList, on_delete=models.CASCADE, related_name='friends')
    sender= models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='sender_msg')
    msg= models.TextField()
    time_sent= models.DateTimeField(default=timezone.now)
