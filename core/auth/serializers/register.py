from rest_framework import serializers
from core.user.serializers import UserSerializer
from core.user.models import User


class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128, min_length=8,
                                     write_only=True, required=True)
    
    class Meta :
        model = User
        #Matnsach bio w avatar
        fields = ['id', 'username', 'first_name',
        'last_name', 'email','password']
    
    def create(slef,validated_data):
        return User.objects.create_user(**validated_data)
        