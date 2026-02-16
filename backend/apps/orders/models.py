"""
Meal order models.
"""
import uuid
from django.db import models
from apps.tenants.models import Tenant
from apps.residents.models import Resident
from apps.menus.models import Menu, MenuItem
from apps.users.models import User
class MealOrder(models.Model):
"""Meal order for a resident."""
id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='orders')
menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
order_date = models.DateField()
meal_type = models.CharField(max_length=20)

is_submitted = models.BooleanField(default=False)
submitted_at = models.DateTimeField(null=True, blank=True)
submitted_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='submitted_orders')

is_locked = models.BooleanField(default=False)
locked_at = models.DateTimeField(null=True, blank=True)

notes = models.TextField(blank=True)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_orders')
version = models.IntegerField(default=0)

class Meta:
    db_table = 'meal_orders'
    unique_together = ['tenant', 'resident', 'order_date', 'meal_type']
    ordering = ['-order_date', 'meal_type']
    indexes = [
        models.Index(fields=['tenant', 'order_date']),
        models.Index(fields=['resident', 'order_date']),
    ]

def __str__(self):
    return f"{self.resident} - {self.order_date} {self.meal_type}"
class MealOrderComponent(models.Model):
"""Individual components of a meal order."""
id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
meal_order = models.ForeignKey(MealOrder, on_delete=models.CASCADE, related_name='components')
menu_item = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True, blank=True)
component_type = models.CharField(max_length=50)
quantity = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)
texture_modification = models.CharField(max_length=100, blank=True)
special_instructions = models.TextField(blank=True)
created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    db_table = 'meal_order_components'
    indexes = [
        models.Index(fields=['tenant', 'meal_order']),
    ]

def __str__(self):
    return f"{self.meal_order} - {self.component_type}"
