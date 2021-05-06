from django.shortcuts import render, redirect, get_object_or_404
import json
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
from django.forms.models import model_to_dict 
from django.http import JsonResponse


# Create your views here.
#views.py code for news feed feature
def NewsFeed(request):
    ArrangedPosts=queue()
    counter=1
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

            for post in postsArray:
                ArrangedPosts.enqueue(post)
                    
            while not ArrangedPosts.isEmpty():
                postList.append(ArrangedPosts.front())
                ArrangedPosts.dequeue()
            break    
                
        while counter != 5:
            for i in friends:
                friendpost.append(i)
        
        for F in friendpost:
            Fposts= Posts.objects.filter(author=F)
            for post in Fposts:
                postsArray.append(post)
        
        for post in postsArray:
            ArrangedPosts.enqueue(post)
                    
        while not ArrangedPosts.isEmpty():
                postList.append(ArrangedPosts.front())
                ArrangedPosts.dequeue()

        
        

        time.sleep(72000) 
       
        for F in postList:
            if F.date_of_release > datetime.now()+timedelta(hours=48):
                postList.remove(F)
        
    postList.reverse()            
    context= {
            
            'postList':postList,
            
           }
    return render(request, 'posts/home.html', context)


def postDetail(request, pk):
    post= get_object_or_404(Posts, pk=pk)
    comments= post.comments.all()
    NumComment= comments.count()
    if request.method =='POST':
        form= CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.by= request.user
            com= form.save(commit=False)
            com.post=post
            com.save()
            return redirect('post-detail',pk=post.pk)
            messages.success(request, f'Commment successful')
    else:
        form= CommentForm()
    context = {
            'post':post,
            'comments':comments,
            'form':form,
            'NumComment':NumComment
            }
    return render(request, 'posts/post-detail.html', context)



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Posts
    template_name='posts/post-form.html'
    fields = ['body','post_image']

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
    template_name='posts/post-delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
def like_post(request):
    if request.method == 'GET':
        result=''
        col='red'
        lat='fas'
        odd='far'
        i=0
        like= request.GET.get('serializedVall')
        liker= Posts.objects.get(pk=like)
        if liker.like.filter(pk=request.user.pk).exists():
            liker.like.remove(request.user)
            liker.like_count -= 1
            result= liker.like_count
            liker.save()
            col=''
            lat='far'
            odd='fas'
        else:
            liker.like.add(request.user)
            liker.like_count += 1
            result= liker.like_count
            liker.save()
        if result == 0:
            result=''
        return JsonResponse({'result':result,'col':col,'lat':lat,'odd':odd}, status=200)
    else:
        return JsonResponse({}, status=400)



