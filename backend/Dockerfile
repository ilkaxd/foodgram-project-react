FROM python:3.8.5

WORKDIR /code

COPY . . 
RUN pip3 install -r requirements.txt 

CMD gunicorn config.wsgi:application --bind 0.0.0.0:8000