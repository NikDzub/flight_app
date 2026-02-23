import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:8000',
});

export const getFlightOffers = async (params) => {
  try {
    const response = await API.get('/flights/offers', { params });
    return response.data;
  } catch (error) {
    console.error('Flight API Error:', error);
    return null;
  }
};
