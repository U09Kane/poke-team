from fastapi import APIRouter

from .pokemon import router as poke_router


router = APIRouter(prefix='/v1')
router.include_router(poke_router)
