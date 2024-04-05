"""
Database models
"""
from django.db import models
from django.contrib.auth.models import (
	AbstractBaseUser,
	BaseUserManager,
	PermissionsMixin,
)


class UserManager(BaseUserManager):
	"""Manager for users"""

	def create_user(self, email, password=None, **extra_fields):
		"""Create. save and return a new user"""
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)

		return user



class User(AbstractBaseUser, PermissionsMixin):
	"""User in the system."""
	email = models.EmailField(max_length=255, unique=True)
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email' #this is how the default username field that comes with default user model is replaced with the field of our choice


##this self.model in the database is essentially maaping our own user model to that of its build in model
##self._db is merely used to provide support for multiple databases.