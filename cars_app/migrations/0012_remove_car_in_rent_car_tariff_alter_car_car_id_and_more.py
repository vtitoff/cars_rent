# Generated by Django 4.2.4 on 2023-08-09 17:10

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("cars_app", "0011_cartariff_remove_car_in_rent_alter_car_car_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="car_id",
            field=models.CharField(
                default=uuid.UUID("46280253-5f58-4728-9812-21fbf5e02609"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="deal",
            name="deal_id",
            field=models.CharField(
                default=uuid.UUID("b21ec3f4-5d65-47b8-a7f3-d24f6234968f"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                default=uuid.UUID("c48687ff-86a7-426b-86a6-6bd403f2d8cf"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
