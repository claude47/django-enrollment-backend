from django.urls import path
from .views import Register, Login, GetUser, ListUsers

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('user/<int:pk>/', GetUser.as_view(), name='get_user'), 
    path('users/', ListUsers.as_view(), name='list_users')
]
