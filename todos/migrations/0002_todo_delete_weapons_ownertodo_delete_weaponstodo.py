# Generated by Django 4.1.7 on 2023-02-26 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Todo",
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
                ("subject", models.CharField(max_length=100)),
                ("details", models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(name="Weapons_OwnerTodo",),
        migrations.DeleteModel(name="WeaponsTodo",),
    ]