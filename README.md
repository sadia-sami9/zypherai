# ZypherAI — SDE Assessment Project

This project implements a FastAPI-based mock prediction server with both synchronous and asynchronous endpoints. It also includes a Dockerfile for containerized deployment.

---

## 🔧 Technologies

- Python 3.13
- FastAPI
- Uvicorn
- Docker

---

## 🚀 How to Run

### 🖥️ Option 1: Docker (Recommended)

```bash
docker build -t zypherai .
docker run -p 8080:8080 zypherai
