# app/main.py
from fastapi import FastAPI, Request, Header, HTTPException
from pydantic import BaseModel
from app.mock_model import mock_model_predict
from app.prediction_store import create_prediction_task, get_prediction
from fastapi.responses import JSONResponse


app = FastAPI()

class InputData(BaseModel):
    input: str

@app.post("/predict")
def predict(
    input_data: InputData,
    request: Request,
    x_async_mode: str = Header(default="false", alias="X-Async-Mode")
):
    print(f"[DEBUG] Headers Received: {request.headers}")
    print(f"[DEBUG] x_async_mode header received: {x_async_mode}")
    
    if x_async_mode.lower() == "true":
        prediction_id = create_prediction_task(input_data.input)
        return JSONResponse(
            status_code=202,
            content={
                "message": "Request received. Processing asynchronously.",
                "prediction_id": prediction_id
            }
        )
    else:
        output = mock_model_predict(input_data.input)
        return output



@app.get("/predict/{prediction_id}")
def get_result(prediction_id: str):
    status, data = get_prediction(prediction_id)
    if status == "not_found":
        raise HTTPException(status_code=404, detail="Prediction ID not found.")
    elif status == "processing":
        raise HTTPException(status_code=400, detail="Prediction is still being processed.")
    return {"prediction_id": prediction_id, "output": data}

@app.get("/")
def root():
    return {"message": "Welcome to ZypherAI Prediction Service!"}
