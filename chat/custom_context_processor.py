from .models import *
from friends.models import *




def DisplayNewMessage(request):
    friendsOne=[]
    friendsTwo=[]
    LastChats=[]
    Last_message_sent=[]
    if request.user.is_anonymous:
        pass
    else:
        FriendListOne= FriendList.objects.filter(Accepter=request.user)
        FriendListTwo= FriendList.objects.filter(Added=request.user)
        for F in FriendListOne:
            Fr= F.Added
            friendsOne.append(Fr)
        for F in FriendListTwo:
            Fr= F.Accepter
            friendsTwo.append(Fr)
        for F in friendsOne:
            Fone= FriendListOne.get(Added=F)
            Last= Chat.objects.filter(sender=F)
            Last= Last.filter(messengers=Fone)
            Last= Last.last()
            LastChats.append(Last)
        for F in friendsTwo:
            Fone= FriendListTwo.get(Accepter=F)
            Last= Chat.objects.filter(sender=F)
            Last= Last.filter(messengers=Fone)
            Last= Last.last()
            LastChats.append(Last)
        
        for F in friendsOne:
            Fone= FriendListOne.get(Added=F)
            Last= Chat.objects.filter(sender=request.user)
            Last= Last.filter(messengers=Fone)
            Last=Last.last()
            Last_message_sent.append(Last)
        for F in friendsTwo:
            Fone= FriendListTwo.get(Accepter=F)
            Last= Chat.objects.filter(sender=request.user)
            Last= Last.filter(messengers=Fone)
            Last=Last.last()
            Last_message_sent.append(Last)
        
        for last in Last_message_sent:
            x=0
            if last and LastChats[x]  != None:
                if last.time_sent > LastChats[x].time_sent:
                    LastChats.pop(x)
            x += 1
    
    
            
    
    NumOfMessages= len(LastChats)
    
    return {
        'NumOfMessages':NumOfMessages,
        
        }

def notifications(request):
    NumOfNotifications=0
    if request.user.is_anonymous:
        pass
    else:
        friend_requests= AddFriend.objects.filter(receiver=request.user)
        for F in friend_requests:
            NumOfNotifications += 1
    return {
        'NumOfNotifications':NumOfNotifications,
        
        }