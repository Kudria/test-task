FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    && pip install --no-cache-dir uwsgi

COPY requirements.txt .

RUN pip install --no-cache-dir -r requiremendocker ts.txt

COPY ./src .

COPY uwsgi.ini .

EXPOSE 8000

CMD python manage.py migrate && uwsgi --ini uwsgi.ini