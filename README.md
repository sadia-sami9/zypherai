ZypherAI — SDE Assessment Submission

This is a backend web application for ZypherAI, simulating Machine Learning predictions with both synchronous and asynchronous support. Built using FastAPI and containerized using Docker, this app exposes prediction endpoints and manages background processing without using external services.


Features:

-  `/predict` POST endpoint
    Handles both **synchronous** and **asynchronous** prediction modes
-  `Async-Mode` header support
    Triggers async background prediction with unique `prediction_id`
-  `/predict/{prediction_id}` GET endpoint
    Returns 200 / 400 / 404 based on prediction status
-  Dockerized for container-based execution
-  In-memory store (no persistence needed)


Technologies Used:

- Python 3.13
- FastAPI
- Uvicorn (ASGI server)
- Docker (`python:3.13-slim`)
- Threading for background tasks
- Type hints and clean code structure


 How to Run:

1. Clone or unzip this repo:
cd zypherai

2. Build Docker image:
docker build -t zypherai .

3. Run the container:
docker run -p 8080:8080 zypherai

App is now running at:  
➡️ `http://localhost:8080`

API Endpoints:

1) `POST /predict` – Synchronous Prediction
Request:
```json
{
  "input": "hello model"
}

Response:
{
  "input": "hello model",
  "result": "13456"
}

2) `POST /predict` – Asynchronous Mode
Headers:
X-Async-Mode: true

Response:
{
  "message": "Request received. Processing asynchronously.",
  "prediction_id": "a1b2c3..."
}

3) GET /predict/{prediction_id}
200 OK → if ready

400 Bad Request → if still processing

404 Not Found → if ID invalid

Response (when done):
{
  "prediction_id": "a1b2c3...",
  "output": {
    "input": "hello",
    "result": "19876"
  }
}

Design Notes:
Uses simple in-memory dictionaries to store prediction status and results

Background tasks run via Python threads (threading.Thread)

No external queue system used (permitted for this project)

All logic is encapsulated and testable


📁 Project Structure:
zypherai/
├── app/
│   ├── main.py
│   ├── mock_model.py
│   └── prediction_store.py
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore