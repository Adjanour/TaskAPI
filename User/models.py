"""

"""
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
# Create your models here.




class UserMangager(BaseUserManager):
    """Manager for users"""

    def create_user(self,email,password=None, **extra_fields):
        if not email:
            raise ValueError("You must provide an email address ")
        """Create, save and return a new user"""
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self,email,password):
        """Create save and return a new superuser"""
        user = self.create_user(email,password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

    def get_by_natural_key(self, email):
        return self.get(email=email)

class User(AbstractBaseUser,PermissionsMixin):
    """ User in the system"""

    email = models.EmailField(max_length=255,unique=True)
    username = models.CharField(max_length=255,unique=True)
    first_name = models.CharField(max_length=255)
    other_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(default='1999-10-01')
    gender_id = models.IntegerField(default=0)
    team_id = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserMangager()

    USERNAME_FIELD = 'email'
