from rest_framework import serializers
from .models import *
import re 

from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model= User
        fields = ['username','password']

    def create(self,validated_data):
        user = User.objects.create(username = validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        exclude= ['created_at', 'updated_at']

    
    def validate_email(self,data):
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')  

        
        
        if not re.fullmatch(regex,data):
            raise serializers.ValidationError("Invalid Email Entered") 
        
        if data and Student.objects.filter(email__exact=data).exists():
            raise serializers.ValidationError("Email already exists!")
        
        return data