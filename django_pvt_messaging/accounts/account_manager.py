# Customising the default manager
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as txt_translation


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    """
    def create_user(self, email, password, **other_fields):

        if not email:
            raise ValueError(txt_translation('Enter a valid email address'))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if(other_fields.get('is_superuser') is not True):
            raise ValueError(txt_translation('The is_superuser=True trigger must be enabled for superusers.'))
        
        if(other_fields.get('is_active') is not True):
            raise ValueError(txt_translation('The is_active=True trigger must be enabled for superusers.'))
        
        return self.create_user(email, password, **other_fields)