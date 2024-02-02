from rest_framework import serializers

from core.abstract.serializers import AbstractSerializer
from core.user.serializers import UserSerializer
from core.post.models import Post
from core.user.models import User

class PostSerializer(AbstractSerializer):
    author = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='public_id')
    
    liked = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    
    def get_liked(self,instance):
        request = self.context.get('request',None)
        
        if request is None or request.user.is_anonymous:
            return False
        
    def get_likes_count(self,instance):
        return instance.liked_by.count()
    
    def update(self, instance, validated_data):
        
        if not instance.edited:
            validated_data['edited'] = True
            
        instance = super().update(instance,validated_data)
        
        return instance
    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        author = User.objects.get_object_by_public_id(rep["author"])
        rep['author'] = UserSerializer(author).data
        
        return rep 

    def validate(self, data):
        request_user = self.context["request"].user
        author = data["author"]

        if request_user != author:
            raise serializers.ValidationError("You can't create a post for another user.")

        return data
    
    

    class Meta:
        model = Post
        fields = ['id','author', 'body', 'edited','liked','likes_count', 'created', 'updated']
        read_only_fields = ['edited']
