from django.urls import path
from .views import register, profile

urlpatterns = [
	path('accounts/register/', register, name='register'),
	path('accounts/profile/', profile, name='profile'),
]