# app/services/flight_service.py
from amadeus import ResponseError
from app.services.amadeus_client import amadeus


def search_flight_offers(origin, destination, departure_date, adults=1, max_offers=5):
    """Search for flight offers between origin and destination."""
    try:
        response = amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=destination,
            departureDate=departure_date,
            adults=adults,
            max=max_offers,
        )
        return response.data
    except ResponseError as e:
        # Print status code
        status = getattr(e.response, "status_code", "N/A")
        print(f"AMADEUS ERROR (Flight Offers Search): [{status}] {e}")

        # Print full response body
        try:
            print("FULL RESPONSE BODY:", e.response.body)
        except Exception:
            print("Could not access response body.")

        # Print headers
        try:
            print("HEADERS:", e.response.headers)
        except Exception:
            pass

        # Return empty list or error info
        return []


def flight_offers_pricing(offer):
    """Get pricing for a flight offer object (from Flight Offers Search)."""
    try:
        response = amadeus.shopping.flight_offers.pricing.post(offer)
        return response.data
    except ResponseError as e:
        print("AMADEUS ERROR (Flight Offers Pricing):", e)
        return []


def flight_dates(origin, destination, departure_date):
    """Check available flight dates for a route."""
    try:
        response = amadeus.shopping.flight_dates.get(
            origin=origin, destination=destination, departureDate=departure_date
        )
        return response.data
    except ResponseError as e:
        print("AMADEUS ERROR: [", getattr(e.response, "status_code", "N/A"), "]")

        # Try to print full response body
        try:
            print("FULL RESPONSE BODY:", e.response.body)
        except Exception:
            print("Could not access response body.")

        # Optional: print headers or other info
        try:
            print("HEADERS:", e.response.headers)
        except Exception:
            pass

        return {"error": "Failed to retrieve flight dates from Amadeus"}


def flight_inspiration(origin, max_price=1000):
    """Get destinations under max_price from an origin."""
    try:
        response = amadeus.shopping.flight_destinations.get(
            origin=origin, maxPrice=max_price
        )
        return response.data
    except ResponseError as e:
        print("AMADEUS ERROR (Flight Inspiration):", e)
        return []


def search_airports(keyword):
    """Search for airports or cities."""
    try:
        response = amadeus.reference_data.locations.get(
            keyword=keyword, subType="AIRPORT"
        )
        return response.data
    except ResponseError as e:
        print("AMADEUS ERROR (Airports):", e)
        return []
