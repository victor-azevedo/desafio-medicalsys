from django.urls import path
from users.views import edit_user, home, login, logout, register

urlpatterns = [
    path('users/login', login, name='login'),
    path('users/register', register, name='register'),
    path('users/logout', logout, name='logout'),
    path('users/edit', edit_user, name='edit_user'),
    path('', home, name='home'),
]
