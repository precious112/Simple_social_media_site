from django.shortcuts import render
from .models import Posts
from datetime import datetime, timedelta
import time
from .forms import *
from .queue import queue
from .stack import stack
from friends.models import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    CreateView,
    UpdateView,
    DeleteView
)
# Create your views here.
#views.py code for news feed feature
def NewsFeed(request):
    ArrangedPosts=queue()
    friends=[]
    friendpost=[]
    postsArray=[]
    postList=[]
    FriendListOne= FriendList.objects.filter(Accepter=request.user) 
    FriendListTwo= FriendList.objects.filter(Added=request.user)
    for F in FriendListOne:
        friend= F.Added
        friends.append(friend)
        
    for F in FriendListTwo:
        friend= F.Accepter
        friends.append(friend)
    
    while len(friends) != 0:
        if len(friends) < 5:
            for F in friends:
                friendpost.append(F)
            for F in friendpost:
                Fposts= Posts.objects.filter(author=F)
                for post in Fposts:
                    postsArray.append(post)
            friendpost= list(postsArray)
            for i in range(0,len(friendpost)):
                for j in range(0,len(postsArray)):
                    ArrangedPosts.enqueue(friendpost[i][j])
                    
            while not ArrangedPosts.isEmpty():
                postList.append(ArrangedPosts.front())
                ArrangedPosts.dequeue()
            break
                
        for i in range(5):
            friendpost.append(friends[i])
        
        for F in friendpost:
                Fposts= posts.objects.filter(author=F)
                for post in Fposts:
                    postsArray.append(post)
        friendpost= list(postsArray)
        for i in range(0,len(friendpost)):
                for j in range(0,len(postsArray)):
                    ArrangedPosts.enqueue(friendpost[i][j])
                    
        while not ArrangedPosts.isEmpty():
                postList.append(ArrangedPosts.front())
                ArrangedPosts.dequeue()
                
        time.sleep(72000) 
       
        for F in postList:
            if F.date_of_release > datetime.now()+timedelta(hours=48):
                postList.remove(F)
        
                
    context= {
            
            'postList':postList,
            
           }
    return render(request, 'posts/home.html', context)


def postDetail(request,pk):
    post= get_object_or_404(Posts, pk=pk)
    comments= posts.comments.all()
    com=None
    
    if request.method =='POST':
        form= CommentForm(request.POST, requests.FILES)
        if form.is_valid():
            com= form.save(commit=False)
            com.post=post
            com.save()
            #return redirect('')
            messages.success(request, f'Commment successful')
        else:
            form= CommentForm()
        context = {
            'post':post,
            'com':com,
            'form':form,
            'comments':comments
            
            }



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    fields = ['body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Posts
    fields = ['body']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Posts
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
