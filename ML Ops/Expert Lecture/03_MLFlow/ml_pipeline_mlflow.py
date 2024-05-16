import pandas as pd
import mlflow
import mlflow.sklearn
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
    
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# mlflow set experiment
mlflow.tracking.set_registry_uri("http://127.0.0.1:8000")

mlflow.set_experiment(experiment_name="My MLFlow demo")

with mlflow.start_run(run_name = "run-1") as run:
    
    training_data = pd.read_csv("store_purchase_data.csv")
    X = training_data.iloc[:,:-1].values
    y = training_data.iloc[:,-1].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

    standard_scaler = StandardScaler()
    X_train = standard_scaler.fit_transform(X_train)
    X_test = standard_scaler.transform(X_test)

    
    num_neighbors = 5
    value_p = 2
    mlflow.log_param("num_of_neighbors", num_neighbors)
    mlflow.log_param("p", value_p)
    classifier = KNeighborsClassifier(n_neighbors = num_neighbors, metric = 'minkowski', p = value_p)

    # Model training
    classifier.fit(X_train, y_train)
  
    y_pred = classifier.predict(X_test)

    model_accuracy = accuracy_score(y_test, y_pred)
    print(model_accuracy)

    # log accuracy
    mlflow.log_metric("accuracy", model_accuracy)
    
    # log model
    mlflow.sklearn.log_model(classifier, "model")
