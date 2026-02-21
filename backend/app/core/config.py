import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    AMADEUS_CLIENT_ID = os.getenv("AMADEUS_CLIENT_ID")
    AMADEUS_CLIENT_SECRET = os.getenv("AMADEUS_CLIENT_SECRET")


settings = Settings()
