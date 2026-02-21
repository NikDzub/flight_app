import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

const DEFAULT_CENTER = [40.4168, -3.7038]; // Madrid
const DEFAULT_ZOOM = 6;

export default function FlightMap({ flights }) {
  return (
    <MapContainer
      center={DEFAULT_CENTER}
      zoom={DEFAULT_ZOOM}
      style={{ height: '100vh', width: '100%' }}
    >
      <TileLayer
        // url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
        // attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/">CARTO</a>'
        url="https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />

      {/* Flight markers */}
      {flights.map((flight, index) => (
        <Marker key={index} position={[flight.lat, flight.lng]}>
          <Popup>
            {flight.origin} → {flight.destination} <br />
            {flight.departureDate}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}
