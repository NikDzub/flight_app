import { useState } from 'react';
import { getFlightOffers } from '../api/flights';
import './SearchBar.css';

export default function SearchBar({ onResults }) {
  const [origin, setOrigin] = useState('');
  const [destination, setDestination] = useState('');
  const [date, setDate] = useState('');

  const handleSearch = async () => {
    const data = await getFlightOffers({
      origin,
      destination,
      departure_date: date,
      adults: 1,
    });

    if (data) {
      onResults(data.data);
    }
  };

  return (
    <div className="search-wrapper">
      <div className="search-box">
        {/* <h2>Search Flights</h2> */}

        <input
          placeholder="Origin (MAD)"
          value={origin}
          onChange={(e) => setOrigin(e.target.value.toUpperCase())}
        />

        <input
          placeholder="Destination (PAR)"
          value={destination}
          onChange={(e) => setDestination(e.target.value.toUpperCase())}
        />

        <input
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />

        <button onClick={handleSearch}>Search</button>
      </div>
    </div>
  );
}
