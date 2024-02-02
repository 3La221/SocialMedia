from rest_framework import serializers
from core.abstract.serializers import AbstractSerializer

from core.user.models import User

class UserSerializer(AbstractSerializer):

    
    class Meta :
        model = User
        #Matnsach bio w avatar
        fields = ['id', 'username', 'first_name',
        'last_name', 'email','avatar','bio',
        'is_active', 'created', 'updated']
        read_only_field = ['is_active']