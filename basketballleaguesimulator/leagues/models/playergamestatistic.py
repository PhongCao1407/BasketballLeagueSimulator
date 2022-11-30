from django.db import models
from .game import Games
from .player import Players

class PlayerGameStatistics(models.Model):
    player = models.OneToOneField(Players, models.DO_NOTHING, primary_key=True)
    game = models.ForeignKey(Games, models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'player_game_statistics'
        unique_together = (('player', 'game'),)