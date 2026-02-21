# app/api/routes/locations.py
from fastapi import APIRouter, Query
from app.services.locations_service import (
    search_locations,
    get_nearby_airports,
    get_points_of_interest,
)

router = APIRouter()


@router.get("/")
def get_locations(keyword: str = Query(...)):
    return {"data": search_locations(keyword)}


@router.get("/nearby")
def nearby_airports(
    latitude: float = Query(...),
    longitude: float = Query(...),
):
    return {"data": get_nearby_airports(latitude, longitude)}


# @router.get("/points-of-interest")
# def points_of_interest(
#     latitude: float = Query(...),
#     longitude: float = Query(...),
# ):
#     return {"data": get_points_of_interest(latitude, longitude)}
