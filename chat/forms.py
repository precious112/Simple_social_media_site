from django import forms
from .models import Chat 

class ChatFriend(forms.Form):
	chatsearch = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'search','class':'form-control'}))
    
class message(forms.ModelForm):
    class Meta:
        model = Chat
        fields= ['msg']
        widgets= {
        'msg': forms.Textarea(attrs={'placeholder':'write message...','class': 'form-control form-control-lg','autocomplete':'off','rows':'1','cols':'1'}),
        }