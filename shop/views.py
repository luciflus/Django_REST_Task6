import json
from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework import generics
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework import views
from rest_framework import authentication, permissions
from .permissions import IsProfilePermission


from .models import Category, Item, Order
from .serializers import CategorySerializer, ItemSerializer, OrderSerializer

class CategoryCreateListView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user.author)