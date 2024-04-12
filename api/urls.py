from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('students.urls')),
    path('', include('users.urls')),
    path('', include('subjects.urls')),
    path('', include('enrollment.urls')),
    path('',include('teachers.urls')),
]
