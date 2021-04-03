from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as user_views

urlpatterns = [
    path('', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile', user_views.profile, name='profile'),
    ]