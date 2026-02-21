import axios from 'axios';

const API_BASE = 'http://127.0.0.1:8000'; // FastAPI backend

export const getFlightOffers = async (
  origin,
  destination,
  departureDate,
  adults = 1,
) => {
  try {
    const response = await axios.get(`${API_BASE}/flights/offers`, {
      params: { origin, destination, departure_date: departureDate, adults },
    });
    return response.data.data;
  } catch (err) {
    console.error('Error fetching flight offers:', err);
    return [];
  }
};
