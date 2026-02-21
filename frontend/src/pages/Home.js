import { useState } from 'react';
import FlightMap from '../components/MapContainer';
import SearchBar from '../components/SearchBar';
import { getFlightOffers } from '../api/flights';

export default function Home() {
  const [flights, setFlights] = useState([]);

  const handleSearch = async ({ origin, destination, departureDate }) => {
    const data = await getFlightOffers(origin, destination, departureDate);
    setFlights(data);
  };

  return (
    <div>
      <SearchBar onSearch={handleSearch} />
      <FlightMap flights={flights} />
    </div>
  );
}
