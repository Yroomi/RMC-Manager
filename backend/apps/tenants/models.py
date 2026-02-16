"""
Tenant models for multi-tenant architecture.
Each tenant represents a separate aged care facility.
"""
import uuid
from django.db import models
class Tenant(models.Model):
"""Represents an aged care facility/venue."""
id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
name = models.CharField(max_length=255, help_text="Facility name")
slug = models.SlugField(max_length=100, unique=True, help_text="URL-friendly identifier")
contact_email = models.EmailField()
phone = models.CharField(max_length=20, blank=True)
address = models.TextField(blank=True)
timezone = models.CharField(max_length=50, default='Australia/Perth')
settings = models.JSONField(default=dict, blank=True)
is_active = models.BooleanField(default=True)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'tenants'
    ordering = ['name']

def __str__(self):
    return self.name
class Wing(models.Model):
"""Represents a wing/section within a facility."""
id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='wings')
name = models.CharField(max_length=100)
floor_number = models.IntegerField(null=True, blank=True)
capacity = models.IntegerField(null=True, blank=True, help_text="Number of residents")
is_active = models.BooleanField(default=True)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'wings'
    ordering = ['tenant', 'name']
    unique_together = ['tenant', 'name']
    indexes = [
        models.Index(fields=['tenant', 'is_active']),
    ]

def __str__(self):
    return f"{self.tenant.name} - {self.name}"
class Room(models.Model):
"""Represents a room within a wing."""
id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='rooms')
wing = models.ForeignKey(Wing, on_delete=models.SET_NULL, null=True, blank=True, related_name='rooms')
room_number = models.CharField(max_length=20)
bed_count = models.IntegerField(default=1)
is_active = models.BooleanField(default=True)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'rooms'
    ordering = ['tenant', 'room_number']
    unique_together = ['tenant', 'room_number']
    indexes = [
        models.Index(fields=['tenant', 'wing']),
    ]

def __str__(self):
    return f"Room {self.room_number}"
