from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AddFriend(models.Model):
	sender= models.ForeignKey(User, on_delete=models.CASCADE,related_name='sender_add')
	receiver= models.ForeignKey(User, on_delete=models.CASCADE,related_name='receiver_add')
    
class FriendList(models.Model):
    Accepter= models.ForeignKey(User, on_delete=models.CASCADE,related_name='Acceptor_accept')
    Added= models.ForeignKey(User, on_delete=models.CASCADE,related_name='Added_accept')