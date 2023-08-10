# Generated by Django 4.2.4 on 2023-08-09 15:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("cars_app", "0008_alter_car_car_id_alter_car_car_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="car_id",
            field=models.CharField(
                default=uuid.UUID("0bb27b27-7dab-4df5-8fcf-4a37d861ee9f"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="deal",
            name="deal_id",
            field=models.CharField(
                default=uuid.UUID("fd73a2a9-62ed-4a74-b9f3-d39355aa0d6a"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                default=uuid.UUID("7d95848d-dc41-4272-8854-eb5e29020af3"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]