FROM tiangolo/uwsgi-nginx-flask:python3.9

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY ./src /app
