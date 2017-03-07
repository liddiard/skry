from time import strftime

from django.db import models


class Sport(models.Model):
    """Football, basketball, baseball, etc. We all know what sports are."""

    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class School(models.Model):
    """A school that (in this context) participates in an athletic program."""

    name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.name


class Game(models.Model):
    """A meeting of two Schools to play a game of a Sport."""

    sport = models.ForeignKey('Sport')
    home_team = models.ForeignKey('School', related_name="home")
    opposing_team = models.ForeignKey('School', related_name="opposing")
    date = models.DateField(help_text='Date on which the game happened or '
                                      'will happen.')
    home_score = models.PositiveSmallIntegerField(null=True, blank=True)
    opposing_score = models.PositiveSmallIntegerField(null=True, blank=True)

    def __str__(self):
        return "%s vs. %s on %s" % (self.home_team, self.opposing_team,
                                    strftime('%a, %b %d, %Y'))
