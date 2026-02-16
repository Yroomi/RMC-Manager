"""
Resident models with complete dietary requirements.
"""
import uuid
from django.db import models
from apps.tenants.models import Tenant, Wing, Room
class Resident(models.Model):
"""Aged care resident with dietary profile."""
class DietType(models.TextChoices):
    REGULAR = 'regular', 'Regular'
    DIABETIC = 'diabetic', 'Diabetic'
    RENAL = 'renal', 'Renal'
    LOW_SODIUM = 'low_sodium', 'Low Sodium'
    HALAL = 'halal', 'Halal'
    KOSHER = 'kosher', 'Kosher'
    VEGETARIAN = 'vegetarian', 'Vegetarian'
    VEGAN = 'vegan', 'Vegan'

class IDDSILevel(models.TextChoices):
    LEVEL_0 = 'level_0', 'Level 0 - Thin Liquid'
    LEVEL_1 = 'level_1', 'Level 1 - Slightly Thick'
    LEVEL_2 = 'level_2', 'Level 2 - Mildly Thick'
    LEVEL_3 = 'level_3', 'Level 3 - Moderately Thick'
    LEVEL_4 = 'level_4', 'Level 4 - Pureed'
    LEVEL_5 = 'level_5', 'Level 5 - Minced & Moist'
    LEVEL_6 = 'level_6', 'Level 6 - Soft & Bite-Sized'
    LEVEL_7 = 'level_7', 'Level 7 - Regular'

class MealSize(models.TextChoices):
    SMALL = 'small', 'Small'
    MEDIUM = 'medium', 'Medium'
    LARGE = 'large', 'Large'

id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name='residents')
room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, blank=True, related_name='residents')
wing = models.ForeignKey(Wing, on_delete=models.SET_NULL, null=True, blank=True, related_name='residents')

first_name = models.CharField(max_length=100)
last_name = models.CharField(max_length=100)
date_of_birth = models.DateField(null=True, blank=True)

diet_type = models.CharField(max_length=50, choices=DietType.choices, null=True, blank=True)
iddsi_level = models.CharField(max_length=10, choices=IDDSILevel.choices, null=True, blank=True)
meal_size = models.CharField(max_length=20, choices=MealSize.choices, default=MealSize.MEDIUM)
fluid_restriction_ml = models.IntegerField(null=True, blank=True, help_text="Daily fluid limit in mL")

is_active = models.BooleanField(default=True)
admission_date = models.DateField(null=True, blank=True)
discharge_date = models.DateField(null=True, blank=True)
notes = models.TextField(blank=True)

created_at = models.DateTimeField(auto_now_add=True)
updated_at = models.DateTimeField(auto_now=True)
version = models.IntegerField(default=0)

class Meta:
    db_table = 'residents'
    ordering = ['last_name', 'first_name']
    indexes = [
        models.Index(fields=['tenant', 'is_active']),
        models.Index(fields=['tenant', 'wing']),
    ]

def __str__(self):
    return f"{self.first_name} {self.last_name}"
class ResidentAllergy(models.Model):
"""Resident allergies with hard/soft restrictions."""
class Severity(models.TextChoices):
    MILD = 'mild', 'Mild'
    MODERATE = 'moderate', 'Moderate'
    SEVERE = 'severe', 'Severe'
    ANAPHYLAXIS = 'anaphylaxis', 'Anaphylaxis'

id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
resident = models.ForeignKey(Resident, on_delete=models.CASCADE, related_name='allergies')
allergen = models.CharField(max_length=255)
severity = models.CharField(max_length=20, choices=Severity.choices, null=True, blank=True)
is_hard_restriction = models.BooleanField(default=True, help_text="System blocks if true")
notes = models.TextField(blank=True)
created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    db_table = 'resident_allergies'
    indexes = [
        models.Index(fields=['tenant', 'resident']),
    ]

def __str__(self):
    return f"{self.resident} - {self.allergen}"
