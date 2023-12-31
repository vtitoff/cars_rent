# Generated by Django 4.2.4 on 2023-08-09 17:37

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("cars_app", "0017_alter_car_car_id_alter_deal_deal_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="car_id",
            field=models.CharField(
                default=uuid.UUID("5d8d5d02-5d42-48ad-9958-22dd23943c9b"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="deal",
            name="deal_id",
            field=models.CharField(
                default=uuid.UUID("639e02b1-5afa-44b5-be61-1ff17131f363"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                default=uuid.UUID("a63e6c0b-d6de-4e3c-9908-8d8ee77a4cca"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]
