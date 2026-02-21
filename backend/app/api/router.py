from fastapi import APIRouter
from app.api.routes import flights, locations

api_router = APIRouter()
api_router.include_router(flights.router, prefix="/flights", tags=["Flight Offers"])
api_router.include_router(locations.router, prefix="/locations", tags=["Locations"])
