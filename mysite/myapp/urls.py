from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    
    path("login/", views.login_request, name="login_request"),
    path('signUp/', views.index, name='index'),
    path("home/", views.logout_request, name="logout_request"),
]
