from rest_framework import serializers 
from .models import WeaponsTodo, Weapons_OwnerTodo

class WeaponsTodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WeaponsTodo
        # the fields that should be included in the serialized output
        fields = ['id', 'weapon_name', 
                  'weapon_type', 'weapon_serial_number',
                  'weapon_origin_country', 'weapon_caliber',
                  'weapon_description', 'weapon_state']

class WeaponsOwnerTodoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Weapons_OwnerTodo
        fields = ['id', 'weapon_id',
    'name', 'location_region_country', 
    'organization_political_affiliation_category',
    'organization_political_affiliation_name',
    'active_status', 'date_assigned']