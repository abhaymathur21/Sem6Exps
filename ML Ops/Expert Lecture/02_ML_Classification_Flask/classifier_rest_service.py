from flask import Flask, request
import pickle
import numpy as np
import os

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))
# Set the current working directory to the directory of the script
os.chdir(script_directory)

directory = 'pkl'
model_file = os.path.join(directory, 'classifier.pickle')
scaler_file = os.path.join(directory, 'standard_scaler.pickle')

local_classifier = pickle.load(open(model_file, 'rb'))
local_scaler = pickle.load(open(scaler_file, 'rb'))

app = Flask(__name__)

@app.route('/model', methods=['POST'])
def hello_world():
    request_data = request.get_json(force=True)
    age = request_data["age"]
    salary = request_data["salary"]
    print(age)
    print(salary)
    x_test = None
    x_test_transformed = None
    pred_proba = None
    return "The prediction is {}".format(None)

if __name__ == "__main__":
    None
