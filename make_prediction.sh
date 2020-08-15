#!/usr/bin/env bash

PORT=443
echo "Port: $PORT"

# POST method predict
curl -X GET https://flask-pred-app.azurewebsites.net/predict
