from django.db import models

class Leagues(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'leagues'