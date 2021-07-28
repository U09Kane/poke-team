from fastapi import APIRouter

from .pokemon import router as poke_router
from .teams import router as team_router


router = APIRouter(prefix='/v1')
router.include_router(poke_router)
router.include_router(team_router)
