import peewee as pw
from fastapi.exceptions import HTTPException

from ..models.matchup import MatchupDB  # noqaf401
from ..models.team import TeamDB


def get_team_by_id(team_id: int) -> TeamDB:
    try:
        team = TeamDB.get_by_id(team_id)
        return team
    except pw.DoesNotExist:
        raise HTTPException(404, 'No team found with id = {team_id}')


def get_team_coverage(tream: TeamDB):
    pass
