from typing import List, Optional

from fastapi import APIRouter

from ..models.pokemon import PokemonDB


router = APIRouter(tags=['pokemon'])


@router.get('/pokemon')
def get_all(limit: Optional[int] = 20, offset: Optional[int] = 0) -> List:
    query = PokemonDB.select()\
        .order_by(PokemonDB.number)\
        .limit(limit)\
        .offset(offset)

    pokes = list(query)
    return pokes


@router.post('/pokemon')
def create(pokemon: dict) -> dict:
    return {}
