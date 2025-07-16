FROM python:3.12-slim

WORKDIR /app

RUN pip install uwsgi

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./src .

COPY uwsgi.ini .

EXPOSE 8000

CMD ["uwsgi", "--ini", "uwsgi.ini"]