FROM python:3.8-slim-buster

WORKDIR /app

RUN pip install requests bs4 firebase_admin

COPY . /app

CMD ["python", "crawler.py"]