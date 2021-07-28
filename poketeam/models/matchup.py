from typing import Literal

import peewee as pw

from .. import db


class MatchupDB(pw.Model):
    """Represents the relationship between the types of attacks and their
    effect on a pokemon of a different type. e.g. Fire is strong against
    """
    offense: str = pw.CharField(10)
    defense: str = pw.CharField(10)
    effect: Literal['strong', 'weak', 'neutral', 'none'] = pw.CharField(10)

    class Meta:
        database = db
        table_name = 'Matchup'


db.create_tables([MatchupDB])
matchups = {}

for mu in MatchupDB.select():
    if mu.offense in matchups:
        matchups[mu.offense].add(mu.defense)
    else:
        matchups[mu.offense] = {mu.defense}

__all__ = ['MatchupDB', 'matchups']
