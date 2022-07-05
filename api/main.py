from fastapi import FastAPI, HTTPException, status, Depends
import pickle
import pandas as pd
from sklearn.metrics import classification_report
#from tensorflow import keras
from fastapi.security import HTTPBasic, HTTPBasicCredentials



api = FastAPI()
security = HTTPBasic()

# Initialization of the users database
users_bdd = {
  "alice": "wonderland",
  "bob": "builder",
  "clementine": "mandarine"
}

# "Load test files"
mit_test = pd.read_csv("mitbih_test.csv", header = None)
mit_test_X = mit_test.iloc[:,:-1]
mit_test_y = mit_test.iloc[:,-1]

def get_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    if not(credentials.password == users_bdd.get(username)) :
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@api.get("/LR/test")
def test_LR(index : int, username : str = Depends(get_current_user)):
    """
    Test the Logistic regression with an example in the test set
    """
    lr = pickle.load(open("LR_2.h5", 'rb'))
    prediction_lr = lr.predict(mit_test_X)[index]

    return {index : prediction_lr}

@api.get("/LR/perf")
def perf_LR(username : str = Depends(get_current_user)):
    """
    Get the performance of the Logistic regression model on the whole test set
    """
    lr = pickle.load(open("LR_2.h5", 'rb'))
    class_report = classification_report(mit_test_y, lr.predict(mit_test_X), output_dict=True)

    return class_report

@api.get("/SVM/test")
def test_LR(index : int, username : str = Depends(get_current_user)):
    """
    Test the Support Vector Classification with an example in the test set
    """
    svc = pickle.load(open("SVM.h5", 'rb'))
    prediction_svc = svc.predict(mit_test_X)[index]

    return {index : prediction_svc}

@api.get("/SVM/perf")
def perf_LR(username : str = Depends(get_current_user)):
    """
    Get the performance of the Support Vector Classification model on the whole test set
    """
    svc = pickle.load(open("SVM.h5", 'rb'))
    class_report = classification_report(mit_test_y, svc.predict(mit_test_X), output_dict=True)

    return class_report

#@api.get("/ANN/test")
#def test_LR(index : int, username : str = Depends(get_current_user)):
#    """
#    Test the Artifial Neural Network with an example in the test set
#    """
#    ann = keras.models.load_model("ANN_1.h5")
#    prediction_ann = ann.predict(mit_test_X).argmax(1)[index]

#    return {index : prediction_ann}

#@api.get("/ANN/perf")
#def perf_LR(username : str = Depends(get_current_user)):
#    """
#    Get the performance of the Artifial Neural Network on the whole test set
#    """
#    ann = keras.models.load_model("ANN_1.h5")
#    class_report = classification_report(mit_test_y, ann.predict(mit_test_X).argmax(1), output_dict=True)

#    return class_report

#@api.get("/CNN/test")
#def test_LR(index : int, username : str = Depends(get_current_user)):
#    """
#    Test the Convolutionnal Neural Network with an example in the test set
#    """
#    cnn = keras.models.load_model("CNN_1.h5")
#    prediction_cnn = cnn.predict(mit_test_X).argmax(1)[index]

#    return {index : prediction_cnn}

#@api.get("/CNN/perf")
#def perf_LR(username : str = Depends(get_current_user)):
#    """
#    Get the performance of the Convolutionnal Neural Network on the whole test set
#    """
#    cnn = keras.models.load_model("CNN_1.h5")
#    class_report = classification_report(mit_test_y, cnn.predict(mit_test_X).argmax(1), output_dict=True)

#    return class_report