# Generated by Django 4.2.4 on 2023-08-09 17:12

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("cars_app", "0002_cartariff_manufacturer_remove_car_in_rent_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="CarTariff",
            fields=[
                (
                    "name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                ("cost_per_hour", models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name="Manufacturer",
            fields=[
                (
                    "name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.RemoveField(
            model_name="car",
            name="in_rent",
        ),
        migrations.AddField(
            model_name="car",
            name="car_status",
            field=models.CharField(
                choices=[
                    ("STANDBY", "standby"),
                    ("RENTED", "rented"),
                    ("RESERVED", "reserved"),
                    ("IN_THE_SERVICE", "in the service"),
                    ("UNAVAILABLE", "unavailable"),
                ],
                default="STANDBY",
                max_length=50,
            ),
        ),
        migrations.AddField(
            model_name="deal",
            name="status",
            field=models.CharField(
                choices=[
                    ("NEW", "new"),
                    ("IN_PROGRESS", "in_progress"),
                    ("CANCELLED", "cancelled"),
                    ("FINISHED", "finished"),
                ],
                default="NEW",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_id",
            field=models.CharField(
                default=uuid.UUID("4bdf7828-d441-4310-ad63-e0f9b862dda5"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="license_number",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="deal",
            name="deal_id",
            field=models.CharField(
                default=uuid.UUID("0f3edcca-9453-4523-87a6-09558cb3c61c"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="driver_license",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="middle_name",
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                default=uuid.UUID("2130020c-ab79-4e89-9abe-745f61ec5707"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.CreateModel(
            name="CarModel",
            fields=[
                (
                    "name",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                (
                    "manufacturer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cars_app.manufacturer",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="car",
            name="tariff",
            field=models.ForeignKey(
                default="DEFAULT",
                on_delete=django.db.models.deletion.PROTECT,
                to="cars_app.cartariff",
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_model",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cars_app.carmodel"
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="manufacturer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cars_app.manufacturer"
            ),
        ),
    ]
