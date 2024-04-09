from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

class Register(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class Login(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            # Generate a token for the user
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key, "detail": "Login successful"})
        return Response({"detail": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

class GetUser(RetrieveAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        permission_classes = [IsAuthenticated]

class ListUsers(ListAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        permission_classes = [IsAuthenticated]