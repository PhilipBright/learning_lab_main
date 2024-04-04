FROM python:3.6-slim-buster

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000


CMD ["python3", "app.py", "--host=0.0.0.0"]

