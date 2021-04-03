from django import forms
from .models import Chat 

class ChatFriend(forms.Form):
	chatsearch = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'search','class':'form-control'}))
    
class message(forms.ModelForm):
    class Meta:
        model = Chat
        fields= ['msg']
        widgets= {
        'msg': forms.TextInput(attrs={'placeholder':'write message...','class': 'form-control'}),
        }