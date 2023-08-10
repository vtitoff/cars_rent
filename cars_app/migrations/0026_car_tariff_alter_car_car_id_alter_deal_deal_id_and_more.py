# Generated by Django 4.2.4 on 2023-08-10 18:14

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("cars_app", "0025_car_tariff_alter_car_car_id_alter_deal_deal_id_and_more"),
    ]

    operations = [
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
            name="car_id",
            field=models.CharField(
                default=uuid.UUID("fd3f71b8-f998-43b2-9d8c-45d569c90e68"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="deal",
            name="deal_id",
            field=models.CharField(
                default=uuid.UUID("c50f5709-3c4c-47d5-8217-78a404c24223"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                default=uuid.UUID("e832dfa5-359e-4395-b994-7af1aeee452a"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]