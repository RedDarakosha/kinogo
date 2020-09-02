from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from .managers import CustomAccountManager
# Create your models here.

class Account(AbstractBaseUser, PermissionsMixin):
	email 			=		models.CharField(max_length=64, unique=True)
	password		=		models.CharField(max_length=128, unique=True)
	username 		= 		models.CharField(max_length=32, blank=True, null=True)

	created_at		=		models.DateTimeField(auto_now_add=True)
	last_login 		=		models.DateTimeField(auto_now_add=True)

	profile 		=		models.ImageField(upload_to='account/profile', blank=True, null=True)

	is_staff 		=		models.BooleanField(default=False)
	is_active		=		models.BooleanField(default=True)
	is_superuser	=		models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRE_FIELDS = ['password']

	objects = CustomAccountManager()

	class Meta:
		verbose_name = 'Account'
		verbose_name_plural = 'Accounts'

	def __str__(self):
		if self.username != None:
			return self.username
		else:
			return self.email