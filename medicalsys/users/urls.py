from django.urls import path
from users.views import home, login, logout, register

urlpatterns = [
    path('users/login', login, name='login'),
    path('users/register', register, name='register'),
    path('users/logout', logout, name='logout'),
    path('', home, name='home'),
]
