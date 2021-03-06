"""precido URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from users import views as user_views
from posts.views import *
from posts import views as p_views
from friends import views as f_views
from chat import views as pc_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('posts/home.html', p_views.NewsFeed, name='posts-home'),
    path('posts/<int:pk>/', p_views.postDetail, name='post-detail'),
    path('posts/new/', p_views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/delete/', p_views.PostDeleteView.as_view(), name='post-delete'),
    path('posts/like/', p_views.like_post, name='like_post'),
    path('friends/search.html', f_views.search, name='friends-search'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('friends/add-friend/', f_views.SearchDetail, name='friends-search-detail'),
    path('friends/accept-requests/', f_views.AcceptRequests, name='accept-requests'),
    path('friends/accept-requests-detail/', f_views.AcceptRequestsDetail, name='accept-requests-detail'),
    path('chat/', include('chat.urls')),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)