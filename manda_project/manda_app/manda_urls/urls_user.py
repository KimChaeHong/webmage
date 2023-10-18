from django.urls import path
from django.contrib.auth import views as auth_views
from ..manda_views import views_users

urlpatterns = [
    path('login/', views_users.user_login, name='login'), 
]