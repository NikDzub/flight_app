# app/services/locations_service.py
from amadeus import ResponseError
from app.services.amadeus_client import amadeus


def search_locations(keyword: str, sub_type: str = None):
    """Search for cities or airports by keyword."""
    try:
        params = {"keyword": keyword}
        if sub_type:
            params["subType"] = sub_type  # e.g., "AIRPORT" or "CITY"

        response = amadeus.reference_data.locations.get(**params)
        return response.data

    except ResponseError as e:
        status = getattr(e.response, "status_code", "N/A")
        print(f"AMADEUS ERROR (Search Locations): [{status}] {e}")
        try:
            print("FULL RESPONSE BODY:", e.response.body)
        except Exception:
            print("Could not access response body.")
        try:
            print("HEADERS:", e.response.headers)
        except Exception:
            pass
        return []


def get_nearby_airports(latitude: float, longitude: float):
    """Get nearby airports based on coordinates."""
    try:
        response = amadeus.reference_data.locations.airports.get(
            latitude=latitude, longitude=longitude
        )
        return response.data

    except ResponseError as e:
        status = getattr(e.response, "status_code", "N/A")
        print(f"AMADEUS ERROR (Nearby Airports): [{status}] {e}")
        try:
            print("FULL RESPONSE BODY:", e.response.body)
        except Exception:
            print("Could not access response body.")
        try:
            print("HEADERS:", e.response.headers)
        except Exception:
            pass
        return []


# def get_points_of_interest(latitude, longitude):
#     """Get points of interest near coordinates using raw endpoint."""
#     try:
#         response = amadeus.get(
#             f"/v1/reference-data/locations/pois",
#             params={"latitude": latitude, "longitude": longitude},
#         )
#         return response.data

#     except ResponseError as e:
#         status = getattr(e.response, "status_code", "N/A")
#         print(f"AMADEUS ERROR (Points of Interest): [{status}] {e}")
#         try:
#             print("FULL RESPONSE BODY:", e.response.body)
#         except Exception:
#             print("Could not access response body.")
#         try:
#             print("HEADERS:", e.response.headers)
#         except Exception:
#             pass
#         return []
