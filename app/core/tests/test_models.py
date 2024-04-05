"""
Tests for models
"""
from django.test import TestCase
from django.contrib.auth import get_user_model

 class ModelTests(TestCase):
 	"""Test Models"""

 	def test_create_user_with_email_successful(self):
 		"""Test creating a user with email is successful."""
 		email = 'test@example.com'
 		password = 'testpass123'
 		user = get_user_model().objects.create_user(
 			email=email,
 			password=password,
 		)

 		self.assertEqual(user.email, email)
 		self.assertTrue(user.check_password(password)) #assertequal is not used because we need to compare witht the hashed password
 		