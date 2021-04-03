from django.db import models
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Posts(models.Model):
	body= models.TextField()
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	date_of_release= models.DateTimeField()
	post_image= models.ImageField(upload_to='post_imgs')
	
	def get_absolute_url(self):
		return reverse('posts-detail', kwargs={'pk': self.pk})
	
class Comment(models.Model):
	post= models.ForeignKey(Posts,on_delete=models.CASCADE, related_name='comments')
	body= models.TextField()
	by=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	date_created= models.DateTimeField(default=timezone.now)	