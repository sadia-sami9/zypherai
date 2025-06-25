# app/mock_model.py
import time
import random
from typing import Dict

# Simulates a time-consuming model prediction with random result
def mock_model_predict(input: str) -> Dict[str, str]:
    # Simulate model delay between 10 and 17 seconds
    time.sleep(random.randint(10, 17))  # Simulate processing delay
    # Generate random prediction result
    result = str(random.randint(1000, 20000))
    # Return input and fake prediction result
    return {"input": input, "result": result}
