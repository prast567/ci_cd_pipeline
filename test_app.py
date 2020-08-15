import json
import requests
def test_app_up():
    url = 'https://flask-pred-app.azurewebsites.net/'
    response = requests.get(url)
    assert response.status_code == 200
    
def test_predict():
    data = {"CHAS":{"0":0},"RM":{"0":6.575},"TAX":{"0":296.0},"PTRATIO":{"0":15.3},"B":{"0":396.9},"LSTAT":{"0":4.98}}
    url = 'https://flask-pred-app.azurewebsites.net:443/predict'
    response = requests.post(url, data)
    assert response.status_code == 200
    
