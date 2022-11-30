from django.db import models
from .player import Players

class PlayerOverallStatistics(models.Model):
    player = models.OneToOneField(Players, models.DO_NOTHING, primary_key=True)
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
        db_table = 'player_overall_statistics'

