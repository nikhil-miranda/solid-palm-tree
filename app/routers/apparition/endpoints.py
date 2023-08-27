import json

from fastapi import APIRouter

router = APIRouter()


@router.get("/apparition/title")
def title_generator():
    # with open("./datasets/dota_2_heroes.json", "r") as f:
    #     data = json.load(f)

    return {"title": "dum dum"}