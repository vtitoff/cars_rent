# Generated by Django 4.2.4 on 2023-08-09 17:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("cars_app", "0020_cartariff_alter_car_car_id_alter_deal_deal_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="car",
            name="car_id",
            field=models.CharField(
                default=uuid.UUID("3d903c17-81b7-4a9b-9423-024120182825"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="deal",
            name="deal_id",
            field=models.CharField(
                default=uuid.UUID("9d90c684-7713-40e5-8576-46c041dc44bd"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.CharField(
                default=uuid.UUID("aeacca48-473b-4466-b859-406576282801"),
                max_length=200,
                primary_key=True,
                serialize=False,
            ),
        ),
    ]