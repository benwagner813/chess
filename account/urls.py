from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True)),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]