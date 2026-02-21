# app/api/routes/flights.py
from fastapi import APIRouter, Body, Query
from app.services.flight_service import (
    search_flight_offers,
    flight_offers_pricing,
    flight_dates,
    flight_inspiration,
    search_airports,
)

router = APIRouter()


@router.get("/offers")
def get_offers(
    origin: str = Query(...),
    destination: str = Query(...),
    departure_date: str = Query(...),
    adults: int = Query(1),
):
    return {"data": search_flight_offers(origin, destination, departure_date, adults)}


@router.post("/offers/pricing")
def get_offer_pricing(offer: dict = Body(...)):
    """Get pricing for a flight offer object"""
    return {"data": flight_offers_pricing(offer)}


@router.get("/flight-dates")
def get_flight_dates(
    origin: str = Query(...),
    destination: str = Query(...),
    departure_date: str = Query(...),
):
    return {"data": flight_dates(origin, destination, departure_date)}


@router.get("/inspiration")
def get_inspiration(origin: str = Query(...), max_price: int = Query(1000)):
    return {"data": flight_inspiration(origin, max_price)}


@router.get("/airports")
def get_airports(keyword: str = Query(...)):
    return {"data": search_airports(keyword)}
