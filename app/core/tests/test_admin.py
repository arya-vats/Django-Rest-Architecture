"""
Test for the django admin modification
"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

class AdminSiteTests(TestCase):
	"""Tests for Django admin"""

	def setUp(self):
		"""Create user and client."""
		self.client = Client()
		self.admin_user = get_user_model().objects.create_superuser(
			email="admin@example.com",
			password="testpass123",
		)
		self.client.force_login(self.admin_user) #this means that any request we make to the client will be made by this user
		self.user = get_user_model().objects.create_user(
			email="user@example.com",
			password="testpass123",
			name="Test User",
		)