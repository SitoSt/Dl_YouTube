FROM python:3

WORKDIR /app

COPY requirements.txt .

RUN python3 -m pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD gunicorn -b 0.0.0.0:8080 wsgi:app