# Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY app-core/ ./app-core/
COPY .env ./

RUN pip install --no-cache-dir requests python-dotenv

CMD ["python", "app-core/main.py"]
