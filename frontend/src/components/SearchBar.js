import { useState } from 'react';

export default function SearchBar({ onSearch }) {
  const [origin, setOrigin] = useState('');
  const [destination, setDestination] = useState('');
  const [departureDate, setDepartureDate] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onSearch({ origin, destination, departureDate });
  };

  return (
    <form
      onSubmit={handleSubmit}
      style={{ display: 'flex', gap: '8px', padding: '10px' }}
    >
      <input
        placeholder="Origin"
        value={origin}
        onChange={(e) => setOrigin(e.target.value)}
      />
      <input
        placeholder="Destination"
        value={destination}
        onChange={(e) => setDestination(e.target.value)}
      />
      <input
        type="date"
        value={departureDate}
        onChange={(e) => setDepartureDate(e.target.value)}
      />
      <button type="submit">Search</button>
    </form>
  );
}
