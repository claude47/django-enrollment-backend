from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('students.urls')),
    path('', include('users.urls')),
]
