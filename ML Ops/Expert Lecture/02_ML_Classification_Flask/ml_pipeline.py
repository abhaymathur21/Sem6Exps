import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import pickle
import os

# Get the directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))
# Set the current working directory to the directory of the script
os.chdir(script_directory)


training_data = pd.read_csv("store_purchase_data.csv")
X = training_data.iloc[:,:-1].values
y = training_data.iloc[:,-1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

standard_scaler = StandardScaler()
X_train = standard_scaler.fit_transform(X_train)
X_test = standard_scaler.transform(X_test)

classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)

# Model training
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

conf_mat = confusion_matrix(y_test, y_pred)
print(conf_mat)
print(accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# Picking the Model and Standard Scaler
directory = 'pkl'
if not os.path.exists(directory):
    os.makedirs(directory)

model_file = os.path.join(directory, 'classifier.pickle')
pickle.dump(classifier, open(model_file, 'wb'))

scaler_file = os.path.join(directory, 'standard_scaler.pickle')
pickle.dump(standard_scaler, open(scaler_file, 'wb'))
