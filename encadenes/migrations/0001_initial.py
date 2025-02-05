# Generated by Django 4.2.14 on 2024-08-06 00:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                ("country", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Crags",
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
                ("crag", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="States",
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
                ("state", models.CharField(max_length=100)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="encadenes.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Sectors",
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
                ("sector", models.CharField(max_length=100)),
                ("total_routes", models.IntegerField()),
                (
                    "crag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="encadenes.crags",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Routes",
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
                ("route", models.CharField(max_length=100)),
                ("rating", models.DecimalField(decimal_places=2, max_digits=3)),
                ("total_ascents", models.IntegerField()),
                ("recommended_by", models.IntegerField()),
                (
                    "sector",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="encadenes.crags",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="crags",
            name="state",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="encadenes.states"
            ),
        ),
    ]
