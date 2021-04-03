from django.urls import path
from . import views as pc_views

urlpatterns = [
    path('chatt/', pc_views.chatt, name='chatt'),
    path('chattdetail/<str:username>/<str:usernamee>/', pc_views.chattdetail, name='chattdetail'),
    path('notifications/', pc_views.notificationsOne, name='notifications'),
    ]