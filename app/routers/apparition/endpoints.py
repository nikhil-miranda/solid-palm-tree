from fastapi import APIRouter

# Adding api endpoint prefix for all routes in this file
router = APIRouter(prefix="/apparition")


@router.get("/title")
def title_generator():
    # with open("./datasets/dota_2_heroes.json", "r") as f:
    #     data = json.load(f)

    return {"title": "dum dum"}
