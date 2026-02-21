# Flight App

This project is a flight search application using **FastAPI** for the backend and **React** for the frontend.  
It integrates with the **Amadeus API** to provide flight offers, airport information, and location data.

---

### Backend

```bash
cd backend
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API docs are available at: http://127.0.0.1:8000/docs
