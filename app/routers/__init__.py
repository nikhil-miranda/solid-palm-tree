from fastapi import APIRouter

from . import apparition, arsenal

router = APIRouter()

router.include_router(apparition.router)
router.include_router(arsenal.router)
