# Midterm Project

## Prerequisites

- Python 3
- Install [Docker](https://www.docker.com/get-started)
- Install [Pipenv](https://github.com/pypa/pipenv)
- Initialise Pipenv and install dependencies: `pipenv install`
- Activate Pipenv: `pipenv shell`

## Train Model

- In order to train a model, run `python3 train.py`

## Run Development Server

Run Flask server in development mode `python3 predict.py`

If you want to test Flask endpoint, send POST request using cURL to `http://localhost:9696/predict` or use `python3 predict-test.py`

## Build & Run Docker

- Build Docker image: `docker build -t cooking_app .`
- If you want to run Docker image, use the following: `docker run -it -p 9696:9696 cooking_app:latest`