from django import forms

class SearchFriend(forms.Form):
	search = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'search','class':'form-control'}))