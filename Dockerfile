# Dockerfile

# 1. Use an official Python slim image
FROM python:3.13-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of the app
COPY . .

# 5. Expose port 8080
EXPOSE 8080

# 6. Run the FastAPI app using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
