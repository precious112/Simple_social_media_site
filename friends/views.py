from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from users.models import Profile
from .forms import SearchFriend
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict 

# Create your views here.
def search(request):
    result=None
    if request.method == 'POST':
        form= SearchFriend(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('search')
            result= User.objects.get(username=name)
    else:
        form= SearchFriend()
    
    friendOne= FriendList.objects.filter(Accepter=request.user, Added=result)
    friendTwo= FriendList.objects.filter(Accepter=result, Added=request.user)
    AddedFriend= AddFriend.objects.filter(sender=request.user, receiver=result)
    AddedFriendTwo= AddFriend.objects.filter(sender=result, receiver=request.user)
    context= {
		'results': result,
        'form':form,
        'friendOne':friendOne,
        'friendTwo':friendTwo,
        'AddedFriend':AddedFriend,
        'AddedFriendTwo':AddedFriendTwo,
		}
    return render(request, 'friends/search.html', context)

def SearchDetail(request):
    Ruser= None
    NewFriendRequest=None
    if request.method == 'GET':
        username= request.GET.get('serializedVal')
        Ruser= User.objects.get(username=username)
        NewFriendRequest=AddFriend.objects.create(sender=request.user,receiver=Ruser)
        NewFriendRequest.save()
        return JsonResponse({"username":model_to_dict(NewFriendRequest)}, status=200)
    else:
        return JsonResponse({},  status=400)
        
	
			
def AcceptRequests(request):
    FriendRequests= AddFriend.objects.filter(receiver=request.user)
    AlreadyFriends= FriendList.objects.filter(Accepter=request.user)
    context= {
	'FriendRequests': FriendRequests,
    'AlreadyFriends':AlreadyFriends,
	}
    return render(request, 'friends/accept-requests.html', context)
	
def AcceptRequestsDetail(request):
    DeleteFriendRequest=None
    Suser=None
    Accepter=None
    if request.method == 'GET':
        username=request.GET.get('serializedVall')
        Suser= User.objects.get(username=username)
        NewAddedFriend= FriendList.objects.create(Accepter=request.user,Added=Suser)
        NewAddedFriend.save()
        DeleteFriendRequest= AddFriend.objects.get(sender=Suser, receiver=request.user)
        DeleteFriendRequest.delete()
        return JsonResponse({"username":model_to_dict(NewAddedFriend)}, status=200)
    else:
        return JsonResponse({},  status=400)
			