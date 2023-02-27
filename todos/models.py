from django.db import models
import uuid

class WeaponsTodo(models.Model):
    weapon_name = models.CharField(max_length=300)
    weapon_type = models.CharField(max_length=300)
    weapon_serial_number = models.CharField(max_length=300)
    weapon_origin_country = models.CharField(max_length=300)
    weapon_caliber = models.CharField(max_length=300)
    weapon_description = models.CharField(max_length=300)
    weapon_state = models.CharField(max_length=300)
    
class Weapons_OwnerTodo(models.Model):
    weapon_id = models.ForeignKey(
        WeaponsTodo,
        on_delete=models.CASCADE,
        null=False
    )
    name = models.CharField(max_length=300)
    location_region_country = models.CharField(max_length=300)
    organization_political_affiliation_category = models.CharField(max_length=300)
    organization_political_affiliation_name = models.CharField(max_length=300)
    active_status = models.CharField(max_length=300)
    date_assigned = models.DateField()