Audit log models - IMMUTABLE.
"""
import uuid
from django.db import models
from apps.tenants.models import Tenant
from apps.users.models import User
class AuditLog(models.Model):
"""Immutable audit trail for all changes."""
id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, null=True, blank=True)
user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

action = models.CharField(max_length=100)  # create, update, delete, override
entity_type = models.CharField(max_length=100)
entity_id = models.UUIDField(null=True, blank=True)

old_value = models.JSONField(null=True, blank=True)
new_value = models.JSONField(null=True, blank=True)

reason = models.TextField(blank=True)
ip_address = models.GenericIPAddressField(null=True, blank=True)
user_agent = models.TextField(blank=True)

created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    db_table = 'audit_logs'
    ordering = ['-created_at']
    indexes = [
        models.Index(fields=['tenant', 'created_at']),
        models.Index(fields=['entity_type', 'entity_id']),
        models.Index(fields=['user']),
    ]

def __str__(self):
    return f"{self.action} - {self.entity_type} - {self.created_at}"

def save(self, *args, **kwargs):
    if self.pk:
        raise ValueError("Audit logs cannot be modified")
    super().save(*args, **kwargs)

def delete(self, *args, **kwargs):
    raise ValueError("Audit logs cannot be deleted")
