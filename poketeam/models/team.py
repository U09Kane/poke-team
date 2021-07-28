from typing import List

import peewee as pw

from .. import db
from .pokemon import PokemonDB


class TeamDB(pw.Model):
    """Team of pokemon. Limited to 6 at most. Has a 1-to-Many relationship
    with TeamMemberDB.
    """
    id: int
    members: List['TeamMemberDB']
    size: int = pw.IntegerField(null=False, default=6)

    class Meta:
        database = db
        table_name = 'Team'


class TeamMemberDB(pw.Model):
    """Many-to-Many Entity representing a pokemon who is part of a
    team of 6 pokemon. Joins Pokemon table to Team table.
    """
    id: int
    position: int = pw.IntegerField(null=False)
    pokemon: PokemonDB = pw.ForeignKeyField(PokemonDB)
    team: TeamDB = pw.ForeignKeyField(TeamDB, backref='members')

    class Meta:
        database = db
        table_name = 'TeamMember'


db.create_tables([TeamDB, TeamMemberDB])
