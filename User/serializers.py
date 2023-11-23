"""Serializers for the user API view"""

from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import gettext as _

import django_filters
from rest_framework import serializers
from User.models import User

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object"""

    class Meta:
        model = get_user_model()
        fields = ['id','email','password','username','first_name','last_name']
        extra_kwargs = {'password':{'write_only':True,'min_length':5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)
    
    def update(self,instance, validated_data):
        """Update and return a user with encrypted password"""
        password = validated_data.pop('password',None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        
        return user
    

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user auth token."""
    email = serializers.EmailField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,                   
    )

    def validate(self,attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password
        )
        if not user:
            msg = _('Unable to authenticate with the provided credentials')
            raise serializers.ValidationError(msg,code='authorization')
        
        attrs['user'] = user


        return attrs

class UserSerializerAll(serializers.ModelSerializer):
    class Meta:
        Model=User
        fields='__all__'      
        

class UserDetailsSerializer(serializers.ModelSerializer):
    # Define a custom field for full name
    full_name = serializers.SerializerMethodField(method_name='get_full_name')

    class Meta:
        model = User  # Replace 'User' with your actual model name
        fields = ['id','last_login','email', 'username', 'first_name', 'other_name', 'last_name', 'date_of_birth', 'team_id', 'is_active', 'is_staff', 'full_name']

    def get_full_name(self, obj) -> str:
        
        """Return the full name of the user"""
        # Combine first name, other name, and capitalized last name into a full name
        last_name = obj.last_name.capitalize() if obj.last_name else ''
        return f"{last_name}, {obj.first_name} {obj.other_name} ".strip()

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'is_active': ['exact'],
            'is_staff': ['exact'],
        }