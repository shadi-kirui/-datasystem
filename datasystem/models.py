# models.py
from django.db import models

# 1. Livestock Farmers
class LivestockFarmer(models.Model):
    name = models.CharField(max_length=255)
    id_no = models.CharField(max_length=20, unique=True, db_index=True)
    phone_no = models.CharField(max_length=15, db_index=True)
    location = models.CharField(max_length=255, db_index=True)
    male_goats = models.PositiveIntegerField(default=0)
    female_goats = models.PositiveIntegerField(default=0)
    weekly_offtake = models.PositiveIntegerField(default=0)
    amount_paid = models.FloatField(default=0.0)
    vaccin_type = models.CharField(max_length=255, blank=True)
    date_administered = models.DateField(null=True, blank=True)
    goats_given = models.PositiveIntegerField(default=0)
    tracking_traceability = models.TextField(blank=True)


    AGE_CHOICES = [
        ('1-6', '1-6 months'),
        ('7-12', '7-12 months'),
        ('13-18', '13-18 months'),
        ('19-25', '19-25 months'),
        ('2.5+', '25 months and above'),
    ]
    WEIGHT_CHOICES = [
        ('1-7', '1-7 kgs'),
        ('8-15', '8-15 kgs'),
        ('16-23', '16-23 kgs'),
        ('24-31', '24-31 kgs'),
        ('32-39', '32-39 kgs'),
        ('40-47', '40-47 kgs'),
        ('48-55', '48-55 kgs'),
    ]

    age_range = models.CharField(max_length=10, choices=AGE_CHOICES, blank=True)
    age_number = models.PositiveIntegerField(default=0)
    weight_range = models.CharField(max_length=10, choices=WEIGHT_CHOICES, blank=True)
    weight_number = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"{self.age_range} | {self.weight_range}: {self.age_count} age_count, {self.weight_count} weight_count"


    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(male_goats__gte=0), name="male_goats_non_negative"),
            models.CheckConstraint(check=models.Q(female_goats__gte=0), name="female_goats_non_negative"),
        ]

# 2. Fodder Farmers
class FodderFarmer(models.Model):
    name = models.CharField(max_length=255)
    id_no = models.CharField(max_length=20, unique=True, db_index=True)
    phone_no = models.CharField(max_length=15, db_index=True)
    location = models.CharField(max_length=255, db_index=True)
    land_acreage_leased = models.FloatField(default=0.0)
    land_acreage_sharing_model = models.TextField(blank=True)
    yield_per_harvest = models.FloatField(default=0.0)
    tugnumber = models.PositiveIntegerField(default=0)
    newbreeding = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

# 3. Infrastructure - Borehole
class Borehole(models.Model):
    location = models.CharField(max_length=255, db_index=True)
    water_used = models.FloatField(default=0.0)
    people_using = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.location

# 3. Infrastructure - Hay Storage
class HayStorage(models.Model):
    bales_stored = models.PositiveIntegerField(default=0)
    bales_given_or_sold = models.PositiveIntegerField(default=0)
    revenue_made = models.FloatField(default=0.0)

    def __str__(self):
        return f"Hay Storage - {self.bales_stored} bales"

# 4. Capacity Building
class CapacityBuilding(models.Model):
    trainings_count = models.PositiveIntegerField(default=0)
    modules = models.TextField(blank=True)

    def __str__(self):
        return f"{self.trainings_count} Trainings"