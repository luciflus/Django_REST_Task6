from datetime import date
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Profile, User

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())],
        write_only=True)
    password = serializers.CharField(
        max_length=20,
        write_only=True)
    password2 = serializers.CharField(
        max_length=20,
        write_only=True)

    class Meta:
        model = Profile
        # fields = "__all__"
        exclude = ['user', ]

    def create(self, validated_data):
        user = User(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        profile = Profile.objects.create(
            name=validated_data['name'],
            user=user
        )
        return profile

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords must be identical")
        return data