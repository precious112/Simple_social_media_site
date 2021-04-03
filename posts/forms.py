from django import forms
from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model= Posts
        fields=['body', 'post_image']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields=['body']