# force rebuild
FROM python:3.11.9-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /App

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie des fichers nécessaires
COPY App ./App
COPY best_threshold.joblib .

EXPOSE 8000

CMD ["uvicorn", "App.main:app", "--host", "0.0.0.0", "--port", "8000"]
