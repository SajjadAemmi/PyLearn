import numpy as np


class LinearLeastSquare:
    def __init__(self):
        pass
    
    def fit(self, X, Y):
        # train
        X = X.values.reshape(-1, 1)
        Y = Y.values.reshape(-1, 1)
        # w = شیب خط
        # w = (X.T * X)^-1 * X.T * Y
        self.w = np.matmul(np.linalg.inv(np.matmul(X.T, X)), np.matmul(X.T, Y))
    
    def predict(self, x):
        y_pred = x * self.w
        return y_pred
    
    def evaluate(self, X, Y, loss="MAE"):
        X = X.values.reshape(-1, 1)
        Y = Y.values.reshape(-1, 1)
        
        Y_pred = []
        for i in range(X.shape[0]):
            y_pred = self.predict(X[i])
            Y_pred.append(y_pred)
        
        Y_pred = np.array(Y_pred)
        Error = Y - Y_pred

        if loss == "MAE":
            return np.mean(np.abs(Error))
        elif loss == "MSE":
            return np.mean(Error ** 2)
