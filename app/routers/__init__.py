from fastapi import APIRouter

from . import apparition

router = APIRouter()

router.include_router(apparition.router)



