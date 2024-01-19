# Generated by Django 4.2.6 on 2024-01-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auctions", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("description", models.TextField()),
                (
                    "image",
                    models.URLField(
                        default="https://lh3.googleusercontent.com/proxy/dDdc84j6O0gxfwK95HFTxmPjdMYO1rO9fPnGEDAIH-5eeKFc2u3W__V8of7b79aCc8TaWrv2vBf4r6o9Zg2R7BosdIOOtrXC0u7V74y8gg"
                    ),
                ),
                ("category", models.CharField(default="uncategorized", max_length=100)),
            ],
        ),
    ]