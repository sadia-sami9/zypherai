# app/prediction_store.py
from typing import Dict
from uuid import uuid4

# In-memory store for results and processing status
store: Dict[str, Dict] = {}
processing: Dict[str, bool] = {}

# Starts a background task to simulate async prediction
def create_prediction_task(input_data: str):
    from .mock_model import mock_model_predict

    # Generate a unique ID for the prediction request
    prediction_id = str(uuid4())
    # Mark this prediction as "in progress"
    processing[prediction_id] = True
    store[prediction_id] = {}

    # Define task to simulate slow model processing
    def task():
        result = mock_model_predict(input_data)
        store[prediction_id] = result
        processing[prediction_id] = False

    # Start the task in a background thread
    import threading
    threading.Thread(target=task).start()
    # Return the prediction ID to the user
    return prediction_id

# Returns prediction status and result (if ready)
def get_prediction(prediction_id: str):
    # Invalid ID
    if prediction_id not in store:
        return "not_found", None
    # Still processing
    elif processing.get(prediction_id, False):
        return "processing", None
    # Result ready
    return "done", store[prediction_id]
