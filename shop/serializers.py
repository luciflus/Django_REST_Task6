from rest_framework import serializers

from .models import Category, Item, Order, Profile

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        # exclude = ['profile', ]
        #read_only_fields = ['profile', ]

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        #read_only_fields = ['profile', ]

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        #read_only_fields = ['profile', ]