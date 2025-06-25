# app/main.py
from fastapi import FastAPI, Request, Header, HTTPException
from pydantic import BaseModel
from app.mock_model import mock_model_predict
from app.prediction_store import create_prediction_task, get_prediction
from fastapi.responses import JSONResponse

# Initialize FastAPI app
app = FastAPI()

# Define the request body structure using Pydantic
class InputData(BaseModel):
    input: str

# POST endpoint for synchronous and asynchronous prediction
@app.post("/predict")
def predict(
    input_data: InputData,
    request: Request,
    x_async_mode: str = Header(default="false", alias="X-Async-Mode")
):
    # Log headers for debugging purposes
    print(f"[DEBUG] Headers Received: {request.headers}")
    print(f"[DEBUG] x_async_mode header received: {x_async_mode}")
    
    # If async header is true, run prediction in background
    if x_async_mode.lower() == "true":
        prediction_id = create_prediction_task(input_data.input)
        return JSONResponse(
            status_code=202,
            content={
                "message": "Request received. Processing asynchronously.",
                "prediction_id": prediction_id
            }
        )
    # Otherwise, run synchronously and return result
    else:
        output = mock_model_predict(input_data.input)
        return output


# GET endpoint to retrieve prediction result by ID
@app.get("/predict/{prediction_id}")
def get_result(prediction_id: str):
    status, data = get_prediction(prediction_id)
    # Handle invalid ID
    if status == "not_found":
        raise HTTPException(status_code=404, detail="Prediction ID not found.")
    # Handle case where prediction is still being processed
    elif status == "processing":
        raise HTTPException(status_code=400, detail="Prediction is still being processed.")
    # Return result if ready
    return {"prediction_id": prediction_id, "output": data}

# Root endpoint to verify API is running
@app.get("/")
def root():
    return {"message": "Welcome to ZypherAI Prediction Service!"}
