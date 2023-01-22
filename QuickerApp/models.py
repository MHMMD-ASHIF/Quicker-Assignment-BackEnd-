from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from rest_framework_simplejwt.tokens import RefreshToken

# Create your models here.


class customizedUserManager(BaseUserManager):
    def _create_user(self, email, first_name,password,phoneNumber='', **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        # if not password:
        #     raise ValueError('Password is not provided')

        user = self.model(
            email=self.normalize_email(email),
            # username=username,
            first_name=first_name,
            phoneNumber=phoneNumber,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email,first_name,password,phoneNumber='',  **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        
        return self._create_user(email,first_name, password,phoneNumber, **extra_fields)



    def create_superuser(self, email, first_name,password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, first_name,password, **extra_fields)





class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=255)
    # username = models.CharField(max_length=50, blank=True)
    first_name = models.CharField(max_length=240, blank=True)
    phoneNumber = models.CharField(max_length=50, blank=True)


    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = customizedUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'phoneNumber']

    def __str__(self):
        return self.email

    def tokens(self):
        refresh = RefreshToken.for_user(self)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class ShopList(models.Model):

    ShopName = models.CharField(max_length=100)
    ShopAddress = models.CharField(max_length=350)
    ShopCity = models.CharField(max_length=50)
    ShopPhone = models.CharField(max_length=25)
    ShopImageName = models.CharField(max_length=100)

    def __str__(self):
        return self.ShopName
