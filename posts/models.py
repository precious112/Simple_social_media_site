from django.db import models
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Posts(models.Model):
	body= models.TextField()
	author=models.ForeignKey(User,on_delete=models.CASCADE)
	date_of_release= models.DateTimeField(default=timezone.now)
	post_image= models.ImageField(upload_to='post_imgs')
	like= models.ManyToManyField(User,related_name='likes', blank=True)
	like_count= models.BigIntegerField(default=0)
	
	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	def save(self):
		super().save()

		img= Image.open(self.post_image.path)
		img.save(self.post_image.path)
	
class Comment(models.Model):
	post= models.ForeignKey(Posts,on_delete=models.CASCADE, related_name='comments')
	body= models.TextField()
	by=models.ForeignKey(User, on_delete=models.CASCADE,default=1)
	date_created= models.DateTimeField(default=timezone.now)	