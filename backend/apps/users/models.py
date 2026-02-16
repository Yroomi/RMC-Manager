"""
User models for authentication and authorization.
"""
import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from apps.tenants.models import Tenant
class UserManager(BaseUserManager):
"""Custom user manager."""
def create_user(self, email, password=None, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    user.set_password(password)
    user.save(using=self._db)
    return user

def create_superuser(self, email, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)
    extra_fields.setdefault('role', User.Role.SUPER_ADMIN)
    return self.create_user(email, password, **extra_fields)
class User(AbstractBaseUser, PermissionsMixin):
"""Custom user model with tenant association and roles."""
class Role(models.TextChoices):
    SUPER_ADMIN = 'super_admin', 'Super Admin'
    VENUE_ADMIN = 'venue_admin', 'Venue Admin'
    CARER = 'carer', 'Carer'
    KITCHEN = 'kitchen', 'Kitchen Staff'
    DIETITIAN = 'dietitian', 'Dietitian'
    AUDITOR = 'auditor', 'Auditor'

id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='users', null=True, blank=True)
email = models.EmailField(unique=True)
first_name = models.CharField(max_length=100)
last_name = models.CharField(max_length=100)
role = models.CharField(max_length=50, choices=Role.choices, default=Role.CARER)
is_active = models.BooleanField(default=True)
is_staff = models.BooleanField(default=False)
date_joined = models.DateTimeField(auto_now_add=True)
last_login = models.DateTimeField(null=True, blank=True)
updated_at = models.DateTimeField(auto_now=True)

objects = UserManager()

USERNAME_FIELD = 'email'
REQUIRED_FIELDS = ['first_name', 'last_name']

class Meta:
    db_table = 'users'
    ordering = ['last_name', 'first_name']
    indexes = [
        models.Index(fields=['tenant', 'role']),
        models.Index(fields=['email']),
    ]

def __str__(self):
    return f"{self.get_full_name()} ({self.email})"

def get_full_name(self):
    return f"{self.first_name} {self.last_name}".strip()
