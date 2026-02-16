"""
Menu and menu item models.
"""
import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField
from apps.tenants.models import Tenant
from apps.users.models import User
class Menu(models.Model):
"""Daily menu for a specific meal."""
class MealType(models.TextChoices):
    BREAKFAST = 'breakfast', 'Breakfast'
    LUNCH = 'lunch', 'Lunch'
    DINNER = 'dinner', 'Dinner'
    SUPPER = 'supper', 'Supper'

id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='menus')
date = models.DateField()
meal_type = models.CharField(max_length=20, choices=MealType.choices)
is_published = models.BooleanField(default=False)
published_at = models.DateTimeField(null=True, blank=True)
published_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)

class Meta:
    db_table = 'menus'
    unique_together = ['tenant', 'date', 'meal_type']
    ordering = ['date', 'meal_type']
    indexes = [
        models.Index(fields=['tenant', 'date']),
    ]

def __str__(self):
    return f"{self.date} - {self.meal_type}"
class MenuItem(models.Model):
"""Individual menu item with IDDSI and allergen info."""
class ComponentType(models.TextChoices):
    MAIN = 'main', 'Main Course'
    SOUP = 'soup', 'Soup'
    SANDWICH = 'sandwich', 'Sandwich'
    SALAD = 'salad', 'Salad'
    DESSERT = 'dessert', 'Dessert'
    BEVERAGE = 'beverage', 'Beverage'

id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='items')
component_type = models.CharField(max_length=50, choices=ComponentType.choices)
name = models.CharField(max_length=255)
description = models.TextField(blank=True)
iddsi_levels = ArrayField(models.CharField(max_length=10), blank=True, default=list)
allergens = ArrayField(models.CharField(max_length=100), blank=True, default=list)
portion_size_g = models.IntegerField(null=True, blank=True)
is_available = models.BooleanField(default=True)
created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    db_table = 'menu_items'
    indexes = [
        models.Index(fields=['tenant', 'menu']),
        models.Index(fields=['component_type']),
    ]

def __str__(self):
    return self.name
