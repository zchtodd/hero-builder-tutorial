from django.db import models


class Character(models.Model):
    strength = models.PositiveIntegerField(default=20)
    dexterity = models.PositiveIntegerField(default=20)
    health = models.PositiveIntegerField(default=20)
    intelligence = models.PositiveIntegerField(default=20)
    charisma = models.PositiveIntegerField(default=20)

    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
