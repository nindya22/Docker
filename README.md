# Docker
## 1. Install Docker:
If you haven't already, you need to install Docker on your machine. You can download and install Docker from the official website (https://www.docker.com/get-started).
## 2. Docker Compose and Dockerfile:
### 2.1. Create a "Dockerfile" for Python:
Create a "Dockerfile" to build a Python image that includes your data ingestion script. Here's a sample Dockerfile:
%# Use an official Python runtime as a parent image%
FROM python:3.8

%# Set the working directory in the container%
WORKDIR /app

%# Copy your Python script and any other necessary files into the container%
COPY data_ingestion_script.py /app/

%# Install any required Python packages using pip%
COPY requirements.txt /app/
RUN pip install -r requirements.txt

%# Specify the command to run your data ingestion script%
CMD ["python", "data_ingestion_script.py"]
### 2.2 Create a "docker-compose.yml" file:
Create a "docker-compose.yml" file to define two services: "web" (Python) and "database" (PostgreSQL). Here's an example of a simple "docker-compose.yml" file:
version: '3'

services:
  web:
    build: .
    ports:
      - "8000:8000"  # Adjust the port as needed
    depends_on:
      - database
    links:
      - database

  database:
    image: postgres:13  # You can specify the PostgreSQL version you want to use
    environment:
      POSTGRES_USER: your_user
      POSTGRES_PASSWORD: your_password
      POSTGRES_DB: your_database
In this example, the "web" service is built using the Dockerfile you created, and it depends on the "database" service. You'll need to adjust the PostgreSQL configuration (user, password, database) as per your requirements.

## 3. Data Ingestion Script
### 3.1 Create "data_ingestion_script.py":
In this example, the "web" service is built using the Dockerfile you created, and it depends on the "database" service. You'll need to adjust the PostgreSQL configuration (user, password, database) as per your requirements.

### 3.2  Create "requirements.txt":
If your script depends on any Python packages, create a "requirements.txt" file listing those dependencies.

### 3.3 Include the script and "requirements.txt" in your project directory.
import requests
import pandas as pd

url = 'https://api.opencagedata.com/geocode/v1/json'
api_key = 'a34768ccd55d49cfa29fb5753e2d1486'

countries = population_df['country'].to_list()

countries_list = []
for country in countries:
    params = {'q': country, 'key': api_key} 
    response = requests.get(url,params=params)
    
    json_data = response.json()
    
    components = json_data['results'][0]['components']
    geometry = json_data['results'][0]['geometry']
    
    country_components = {
        'country': country,
        'country_code': components.get('country_code',''),
        'latitude': geometry.get('lat'),
        'longitude': geometry.get('Ing')
    }
    
    countries_list.append(country components)

    component_df = pd.DataFrame(countries_list)

## 4. Run Your Dockerized Application
Open a terminal in your project directory where the "docker-compose.yml" file is located.
Run the following command to build and run your containers:
docker compose up -d
This command will start the containers, and the data ingestion script will be executed as specified in the Dockerfile.

Make sure you have the necessary API access credentials and that the PostgreSQL connection details in the "docker-compose.yml" and your data ingestion script are correctly configured. Adjust the file paths, dependencies, and configurations to match your specific use case.


