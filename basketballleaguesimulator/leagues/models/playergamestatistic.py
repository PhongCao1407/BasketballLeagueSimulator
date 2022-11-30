from django.db import models
from .game import Games
from .player import Players

class PlayerGameStatistics(models.Model):
    player = models.OneToOneField(Players, models.DO_NOTHING, primary_key=True)
    game = models.ForeignKey(Games, models.DO_NOTHING)
    ts = models.IntegerField(default=0)
    reb = models.IntegerField(default=0)
    ast = models.IntegerField(default=0)
    stl = models.IntegerField(default=0)
    blk = models.IntegerField(default=0)
    fg_percentage = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    three_p_percentage = models.DecimalField(max_digits=4, decimal_places=1, default=0)
    ft_percentage = models.DecimalField(max_digits=4, decimal_places=1, default=0)

    class Meta:
        managed = True
        db_table = 'player_game_statistics'
        unique_together = (('player', 'game'),)