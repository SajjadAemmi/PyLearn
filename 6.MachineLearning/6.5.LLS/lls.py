import numpy as np


class LinearLeastSquare:
    def __init__(self):
        pass
    
    def fit(self, X_train, Y_train):
        # train
        X = X_train.reshape(-1, 1)
        Y = Y_train.reshape(-1, 1)
        # w = شیب خط
        # w = (X.T * X)^-1 * X.T * Y
        self.w = np.linalg.inv(X.T @ X) @ X.T @ Y
    
    def predict(self, X_test):
        Y_pred = X_test * self.w
        return Y_pred
    
    def evaluate(self, X_test, Y_test, loss="MAE"):
        X_test = X_test.reshape(-1, 1)
        Y_test = Y_test.reshape(-1, 1)
        
        Y_pred = self.predict(X_test)
        Error = Y_test - Y_pred

        if loss == "MAE":
            return np.mean(np.abs(Error))
        elif loss == "MSE":
            return np.mean(Error ** 2)
