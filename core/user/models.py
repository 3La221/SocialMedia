import uuid
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404

from core.abstract.models import AbstractManager, AbstractModel


class UserManager(BaseUserManager ,AbstractManager):
    

        
        
    def create_user(self,username,email,password=None,**kwargs):
        """Create and return a `User` with an email, phone
            number, username and password."""
        if username is None:
            raise TypeError('User must have username. ')
        if email is None:
            raise TypeError('User must have email. ')
        if password is None:
            raise TypeError('User must have password. ')      
        user = self.model(username=username,email=self.normalize_email(email),**kwargs)
        user.set_password(password)
        user.save(using=self.db)
        
        return user 
    
    def create_superuser(self,username,email,password,**kwargs):
        """Create and return a `User` with superuser (admin)
        permissions."""
        if username is None:
            raise TypeError('User must have username. ')
        if email is None:
            raise TypeError('User must have email. ')
        if password is None:
            raise TypeError('User must have password. ')
        user = self.create_user(username,email,password,**kwargs)       
        user.is_super_user = True 
        user.is_staff  = True
        user.save(using=self.db)

        return user 
    

class User(AbstractBaseUser,PermissionsMixin,AbstractModel):
    username = models.CharField(db_index = True ,max_length = 25 , unique = True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique = True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    posts_liked = models.ManyToManyField("core_post.Post",related_name="liked_by")
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()
    
    def __str__(self):
        return f"{self.email}"
    
    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"    
    
    def like(self, post):
        """Like `post` if it hasn't been done yet"""
        return self.posts_liked.add(post)
    def remove_like(self, post):
        """Remove a like from a `post`"""
        return self.posts_liked.remove(post)
    def has_liked(self, post):
        """Return True if the user has liked a `post`; else False"""
        return self.posts_liked.filter(pk=post.pk).exists()
    
    


