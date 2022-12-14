# Generated by Django 4.1.3 on 2022-11-30 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("leagues", "0002_rename_playerstatistics_playergamestatistics_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="PlayerOverallStatistics",
            fields=[
                (
                    "player",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="leagues.players",
                    ),
                ),
                ("pts", models.DecimalField(decimal_places=1, max_digits=4)),
                ("reb", models.DecimalField(decimal_places=1, max_digits=4)),
                ("ast", models.DecimalField(decimal_places=1, max_digits=4)),
                ("stl", models.DecimalField(decimal_places=1, max_digits=4)),
                ("blk", models.DecimalField(decimal_places=1, max_digits=4)),
                ("fg_percentage", models.DecimalField(decimal_places=1, max_digits=4)),
                (
                    "three_p_percentage",
                    models.DecimalField(decimal_places=1, max_digits=4),
                ),
                ("ft_percentage", models.DecimalField(decimal_places=1, max_digits=4)),
            ],
            options={
                "db_table": "player_overall_statistics",
                "managed": True,
            },
        ),
        migrations.AddField(
            model_name="playergamestatistics",
            name="ast",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="playergamestatistics",
            name="blk",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="playergamestatistics",
            name="fg_percentage",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name="playergamestatistics",
            name="ft_percentage",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name="playergamestatistics",
            name="reb",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="playergamestatistics",
            name="stl",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="playergamestatistics",
            name="three_p_percentage",
            field=models.DecimalField(decimal_places=1, default=0, max_digits=4),
        ),
        migrations.AddField(
            model_name="playergamestatistics",
            name="ts",
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name="PlayerSeasonStatistics",
            fields=[
                (
                    "player",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        primary_key=True,
                        serialize=False,
                        to="leagues.players",
                    ),
                ),
                ("pts", models.DecimalField(decimal_places=1, max_digits=4)),
                ("reb", models.DecimalField(decimal_places=1, max_digits=4)),
                ("ast", models.DecimalField(decimal_places=1, max_digits=4)),
                ("stl", models.DecimalField(decimal_places=1, max_digits=4)),
                ("blk", models.DecimalField(decimal_places=1, max_digits=4)),
                ("fg_percentage", models.DecimalField(decimal_places=1, max_digits=4)),
                (
                    "three_p_percentage",
                    models.DecimalField(decimal_places=1, max_digits=4),
                ),
                ("ft_percentage", models.DecimalField(decimal_places=1, max_digits=4)),
                (
                    "season",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="leagues.seasons",
                    ),
                ),
            ],
            options={
                "db_table": "player_season_statistics",
                "managed": True,
                "unique_together": {("player", "season")},
            },
        ),
    ]
