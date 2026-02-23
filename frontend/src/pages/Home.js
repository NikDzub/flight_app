import { useState } from 'react';
import SearchBar from '../components/SearchBar';
import MapContainer from '../components/MapContainer';

export default function Home() {
  const [flights, setFlights] = useState([]);

  return (
    <>
      <MapContainer flights={flights} />
      <SearchBar onResults={setFlights} />
    </>
  );
}
