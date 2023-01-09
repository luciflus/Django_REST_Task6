from datetime import date
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Profile, User

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        #exclude = ['user', ]
        read_only_fields = ['author', ]