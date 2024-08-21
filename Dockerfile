#image from dockerhub
FROM python:3.8-slim-buster

#commands to be run and the wokrking directory
RUN apt update -y && apt install  awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]


