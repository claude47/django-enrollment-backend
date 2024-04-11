from django.urls import path
from .views import Register, Login, GetUser, ListUsers

urlpatterns = [
    path('register/', Register.as_view()),
    path('login/', Login.as_view()),
    path('user/<int:pk>/', GetUser.as_view()), 
    path('users/', ListUsers.as_view())
]
