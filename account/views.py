from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import viewsets, status
from .models import Profile
from .serializers import ProfileSerializer

class ProfileCreateListView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
