from django.urls import path
from users.views import delete_user, edit_user, home, login, logout, register

urlpatterns = [
    path('users/login', login, name='login'),
    path('users/register', register, name='register'),
    path('users/logout', logout, name='logout'),
    path('users/edit', edit_user, name='edit_user'),
    path('users/delete', delete_user, name='delete_user'),
    path('', home, name='home'),
]
