from locust import Locust,  Taskset
import json
import requests


def index():
    url = 'https://flask-pred-app.azurewebsites.net/'
    response = requests.get(url)
    assert response.status_code == 200


def predict():
    data = {"CHAS": {"0": 0}, "RM": {"0": 6.575}, "TAX": {"0": 296.0}, "PTRATIO": {"0": 15.3}, "B": {"0": 396.9},
            "LSTAT": {"0": 4.98}}
    url = 'https://flask-pred-app.azurewebsites.net:443/predict'
    response = requests.post(url, data)
    assert response.status_code == 200


class test_runner(TaskSet):
    tasks = [index, predict]
    
class main(Locust):
    task_set = test_runner

