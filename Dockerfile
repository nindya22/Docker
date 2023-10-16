# syntax=docker/dockerfile:1
FROM python:3.7-alpine #base image
WORKDIR /code #define directory apps on container
ENV FLASK_APP=app.py #environment variable falsk
ENV FLASK_RUN_HOST=0.0.0.0 #environment variable falsk
RUN apk add --no-cache gcc musl-dev linux-headers #dependencies
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000 
COPY . .
CMD ["flask", "run"] #flask run
