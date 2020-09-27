FROM python:3.6
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN python manage.py collectstatic --noinput
CMD gunicorn wd.wsgi:application --bind 0.0.0.0:8000