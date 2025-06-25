# app/prediction_store.py
from typing import Dict
from uuid import uuid4

store: Dict[str, Dict] = {}
processing: Dict[str, bool] = {}

def create_prediction_task(input_data: str):
    from .mock_model import mock_model_predict

    prediction_id = str(uuid4())
    processing[prediction_id] = True
    store[prediction_id] = {}

    def task():
        result = mock_model_predict(input_data)
        store[prediction_id] = result
        processing[prediction_id] = False

    import threading
    threading.Thread(target=task).start()
    return prediction_id

def get_prediction(prediction_id: str):
    if prediction_id not in store:
        return "not_found", None
    elif processing.get(prediction_id, False):
        return "processing", None
    return "done", store[prediction_id]
