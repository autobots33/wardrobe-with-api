from django.db import models
from django.forms import EmailField
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin 
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.
class UserManager(BaseUserManager):
   use_in_migrations = True

   def create_user(self, phone_number, email, password, **extra_fields):
       if not phone_number:
           raise ValueError('The given phone number must be set')
       user = self.model(phone_number=phone_number, email=self.normalize_email(email), **extra_fields)
       user.set_password(password)
       user.save(using=self._db)
       return user

   def _create_user(self, phone_number, email=None, password=None, **extra_fields):
       extra_fields.setdefault('is_staff', False)
       extra_fields.setdefault('is_superuser', False)
       return self.create_user(phone_number, email, password, **extra_fields)

   def create_superuser(self, phone_number, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_admin') is not True:
            raise ValueError('Superuser must have is_admin=True.')

        return self.create_user(phone_number, email, password, **extra_fields)
    
    


class User(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=50,unique=True) 
    email=models.EmailField( max_length=254,unique=True)
    phone_number= models.CharField(max_length=250, null=True, blank=True, unique=True)    
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

  
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS=['username','phone_number']
    objects = UserManager()

    def __str__(self):
       if self.is_superuser:
           return 'Superuser'
       else:
           # return self.first_name + ' ' + self.last_name
           return self.email
       
@receiver(post_save, sender=settings.AUTH_USER_MODEL)  
def create_auth_token(sender=User, instance=None , created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)    

  
    