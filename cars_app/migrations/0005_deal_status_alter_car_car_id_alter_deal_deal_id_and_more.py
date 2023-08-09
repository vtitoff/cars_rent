# Generated by Django 4.2.4 on 2023-08-09 13:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("cars_app", "0004_alter_car_car_id_alter_deal_deal_id_and_more"),
    ]

    operations = [
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
                default=uuid.UUID("a2ce7a98-5f99-43db-adf5-54e51b29acb8"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="deal",
            name="deal_id",
            field=models.CharField(
                default=uuid.UUID("f501949f-cb1c-488a-9635-0e0fde45d61a"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                default=uuid.UUID("0329fa9d-62e4-4610-bf7d-fc6fc2c60b6e"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
