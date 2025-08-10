# Dockerfile

FROM python:3.11-slim

WORKDIR /app

COPY app-core/ ./app-core/
COPY .env ./
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app-core/main.py"]
