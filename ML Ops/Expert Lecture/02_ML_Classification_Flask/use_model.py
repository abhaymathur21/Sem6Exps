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

x_test = [[42, 50000]]
x_test_transformed = local_scaler.transform(np.array(x_test))
new_prediction = local_classifier.predict(x_test_transformed)
print(new_prediction)
