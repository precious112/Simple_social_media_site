from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
from friends.models import *
# Create your views here.

def chatt(request):
    result= None
    if request.method == 'POST':
        
        form= ChatFriend(request.POST)
        
        if form.is_valid():
            name = form.cleaned_data.get('chatsearch')
            userr = User.objects.get(username=name)
            if FriendList.objects.filter(Accepter=request.user,Added=userr).exists():
                result = FriendList.objects.get(Accepter=request.user,Added=userr)
            else:
                try:
                    result = FriendList.objects.get(Accepter=userr,Added=request.user)
                except FriendList.DoesNotExist:
                    redirect('chatt')
            
                
                
            
                
                
    else:
        form= ChatFriend()
    
   
    
    
    
    context={
           'results': result,
           'form':form,
            }
    
    return render(request, 'chat/chatt.html', context)

def chattdetail(request, username, usernamee):
    Acceptor= User.objects.get(username=username)
    Addid= User.objects.get(username=usernamee)
    friend= FriendList.objects.get(Accepter=Acceptor,Added=Addid)
    chats= friend.friends.all()
    msgg=None
    if request.method == 'POST':
        form= message(request.POST)
        if form.is_valid():
            form.instance.sender= request.user
            msgg=form.save(commit=False)
            if friend.Accepter or friend.Added == request.user:
                msgg.messengers= friend
                msgg.save()
                form= message()
            
            redirect('chattdetail',friend.Accepter.username,friend.Added.username)
    else:
        form= message(instance=request.user)
            
    context={
        'friend':friend,
        'msgs':chats,
        'form':form,
        }
    return render(request, 'chat/search-friend-detail.html', context)
    
    
def notificationsOne(request):
    if request.user.is_anonymous:
        pass
    else:
        friend_requests= AddFriend.objects.filter(receiver=request.user)
    context= {
        'friendrequests':friend_requests,
        
        } 
    return render(request, 'chat/notifications.html', context)
