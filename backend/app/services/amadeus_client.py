from amadeus import Client
from app.core.config import settings

amadeus = Client(
    client_id=settings.AMADEUS_CLIENT_ID,
    client_secret=settings.AMADEUS_CLIENT_SECRET,
    hostname="test",
)
