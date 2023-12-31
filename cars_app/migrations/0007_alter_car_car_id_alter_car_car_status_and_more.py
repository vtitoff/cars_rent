# Generated by Django 4.2.4 on 2023-08-09 13:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        (
            "cars_app",
            "0006_car_car_status_alter_car_car_id_alter_deal_deal_id_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="car_id",
            field=models.CharField(
                default=uuid.UUID("dd4fc855-5439-4d18-b5a6-8bfefc9687de"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="car",
            name="car_status",
            field=models.CharField(
                choices=[
                    ("STANDBY", "standby"),
                    ("WORKING", "working"),
                    ("RESERVED", "reserved"),
                    ("IN_THE_SERVICE", "in the service"),
                    ("UNAVAILABLE", "unavailable"),
                ],
                default="WAITING_CLIENT",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="deal",
            name="deal_id",
            field=models.CharField(
                default=uuid.UUID("7075bc8d-a505-4e2a-8e69-7d4e4939bc8d"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                default=uuid.UUID("00198009-3b15-4737-9a11-523cf836b2f8"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
