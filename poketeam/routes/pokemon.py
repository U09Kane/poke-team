from typing import List, Optional

import peewee as pw
from fastapi import APIRouter, HTTPException

from ..models.pokemon import PokemonDB
from .. import schemas


router = APIRouter(tags=['pokemon'])


@router.get('/pokemon', response_model=List[schemas.Pokemon])
def get_all(limit: Optional[int] = 20, offset: Optional[int] = 0):
    query = PokemonDB.select()\
        .order_by(PokemonDB.number)\
        .limit(limit)\
        .offset(offset)
    return list(query)


@router.get('/pokemon/{pokemon_id}', response_model=schemas.Pokemon)
def get(pokemon_id: int) -> schemas.Pokemon:
    try:
        poke = PokemonDB.get_by_id(pokemon_id)
        return poke
    except pw.DoesNotExist:
        raise HTTPException(404, f'No pokemon with id = {pokemon_id}')
