# Generated by Django 4.1.7 on 2023-02-26 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="WeaponsTodo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("weapon_name", models.CharField(max_length=300)),
                ("weapon_type", models.CharField(max_length=300)),
                ("weapon_serial_number", models.CharField(max_length=300)),
                ("weapon_origin_country", models.CharField(max_length=300)),
                ("weapon_caliber", models.CharField(max_length=300)),
                ("weapon_description", models.CharField(max_length=300)),
                ("weapon_state", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Weapons_OwnerTodo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=300)),
                ("location_region_country", models.CharField(max_length=300)),
                (
                    "organization_political_affiliation_category",
                    models.CharField(max_length=300),
                ),
                (
                    "organization_political_affiliation_name",
                    models.CharField(max_length=300),
                ),
                ("active_status", models.CharField(max_length=300)),
                ("date_assigned", models.DateField()),
                (
                    "weapon_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="todos.weaponstodo",
                    ),
                ),
            ],
        ),
    ]
