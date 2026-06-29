FROM python:3.10-slim-bookworm

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y awscli

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]