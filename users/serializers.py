from rest_framework import serializers
from .models import UserModel
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=50)
    email = serializers.EmailField()
    date_of_birth = serializers.DateField()
    bio = serializers.CharField(max_length=500)
    password = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'})
    password2 = serializers.CharField(min_length=8, write_only=True, style={'input_type': 'password'})

    class Meta:
        model = UserModel
        fields = ('username', 'email', 'date_of_birth', 'bio', 'password', 'password2')

    def validate(self, attrs):
        email_exists = UserModel.objects.filter(email=attrs['email']).exists()

        if email_exists:
            raise ValidationError('Email already exists')

        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise ValidationError('Passwords do not match')

        return super().validate(attrs)

    def create(self, validated_data):
        password = validated_data.pop("password")
        password2 = validated_data.pop("password2")
        if password != password2:
            raise ValidationError('Passwords do not match')

        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)

        return user
