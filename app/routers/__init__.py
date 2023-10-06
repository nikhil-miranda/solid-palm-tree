from fastapi import APIRouter

from . import apparition, arsenal, github

router = APIRouter()

router.include_router(apparition.router)
router.include_router(arsenal.router)
router.include_router(github.router)
