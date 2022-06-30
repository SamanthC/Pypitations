from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC


class Model:
    def __init__(self, name, *args):
        self.name = name
        