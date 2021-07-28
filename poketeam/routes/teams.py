from typing import List

from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
# import peewee as pw

from .. import db
from .. import schemas
from ..models.team import TeamDB, TeamMemberDB
from ..models.pokemon import PokemonDB


router = APIRouter(tags=['teams'])


class TeamDefinition(BaseModel):
    size: int
    members: List[int]


@router.post('/teams', status_code=201)
def create(team_def: TeamDefinition):
    team = TeamDB(size=team_def.size)
    team.save()

    pokes = PokemonDB.select().where(PokemonDB.id << team_def.members)
    entries = []
    for i, poke in enumerate(pokes):
        entries.append(TeamMemberDB(
            position=i + 1,
            pokemon=poke,
            team=team,
        ))
    with db.atomic():
        TeamMemberDB.bulk_create(entries)
    return {'teamId': team.id}


@router.get('/teams/{team_id}', response_model=List[schemas.Pokemon])
def get(team_id: int):
    team = TeamDB.get_by_id(team_id)
    if not team:
        raise HTTPException(404, f'No team found id = {team_id}')

    members = TeamMemberDB.select()\
        .where(TeamMemberDB.team == team)\
        .order_by(TeamMemberDB.position)

    return [m.pokemon for m in members]
