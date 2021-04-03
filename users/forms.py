from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
     
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets= {
        'username': forms.TextInput(attrs={'placeholder':'Username','class': 'form-control'}),
        'email': forms.TextInput(attrs={'placeholder':'Email','class': 'form-control'}),
        'password1': forms.TextInput(attrs={'placeholder':'Password','class': 'form-control'}),
        'password2': forms.TextInput(attrs={'placeholder':'Confirm Password','class': 'form-control'}),
        }
    
class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']