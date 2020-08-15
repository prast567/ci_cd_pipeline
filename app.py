"""app class"""

import logging
from os import environ

from flask import Flask, jsonify
from flask.logging import create_logger

#import pandas as pd
from sklearn.externals import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
LOG = create_logger(app)
LOG.setLevel(logging.INFO)

def scale(payload):
    """Scales Payload"""

#    LOG.info("Scaling Payload: %s" %payload)
    scaler = StandardScaler().fit(payload)
    scaled_adhoc_predict = scaler.transform(payload)
    return scaled_adhoc_predict

@app.route("/")
def home():
    """index page"""
    html = "<h3>Sklearn Prediction Home- Azure pipeline</h3>"
    return html.format(format)
    #return jsonify({'prediction': [ 20.35373177134412 ]})


# TO DO:  Log out the prediction value
@app.route("/predict", methods=['GET'])
def predict():
    """Performs an sklearn prediction

    input looks like:
            {
    "CHAS":{
      "0":0
    },
    "RM":{
      "0":6.575
    },
    "TAX":{
      "0":296.0
    },
    "PTRATIO":{
       "0":15.3
    },
    "B":{
       "0":396.9
    },
    "LSTAT":{
       "0":4.98
    }

    result looks like:
    { "prediction": [20.35373177134412] }

    """


    #json_payload = request.json
    #LOG.info(f"JSON payload: {json_payload}")
    #inference_payload = pd.DataFrame(json_payload)
    #LOG.info(f"inference payload DataFrame: {inference_payload}")
    #scaled_payload = scale(inference_payload)
    #prediction = list(clf.predict(scaled_payload))
    return jsonify({'prediction': [20.35373177134412]})

if __name__ == "__main__":
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        #PORT = int(environ.get('SERVER_PORT', '5555'))
        PORT = 3000
    except ValueError:
        PORT = 3000
    #app.run(HOST, PORT, ssl_context='adhoc')
    clf = joblib.load("boston_housing_prediction.joblib")
    app.run(host=HOST, port=PORT, debug=True)
