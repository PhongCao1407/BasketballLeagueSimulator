from django.db import models
from .player import Players
from .season import Seasons

class PlayerSeasonStatistics(models.Model):
    player = models.OneToOneField(Players, models.DO_NOTHING, primary_key=True)
    season = models.OneToOneField(Seasons, models.DO_NOTHING)
    pts = models.DecimalField(max_digits=4, decimal_places=1)
    reb = models.DecimalField(max_digits=4, decimal_places=1)
    ast = models.DecimalField(max_digits=4, decimal_places=1)
    stl = models.DecimalField(max_digits=4, decimal_places=1)
    blk = models.DecimalField(max_digits=4, decimal_places=1)
    fg_percentage = models.DecimalField(max_digits=4, decimal_places=1)
    three_p_percentage = models.DecimalField(max_digits=4, decimal_places=1)
    ft_percentage = models.DecimalField(max_digits=4, decimal_places=1)

    class Meta:
        managed = True
        db_table = 'player_season_statistics'
        unique_together = (('player', 'season'),)
