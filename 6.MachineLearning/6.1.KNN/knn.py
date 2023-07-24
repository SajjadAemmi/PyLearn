import numpy as np
from sklearn.metrics.pairwise import euclidean_distances


class KNN:
    def __init__(self, k):
        self.k = k
    
    # training
    def fit(self, X, Y):
        self.X_train = X
        self.Y_train = Y

    def predict(self, X):
        Y = []
        for x in X:
            distances = euclidean_distances(x, self.X_train)

            nearest_neighbors = np.argsort(distances)[0:self.k]
            result = np.bincount(self.Y_train[nearest_neighbors])
            y = np.argmax(result)
            Y.append(y)
        return Y

    def evaluate(self, X, Y):
        Y_pred = self.predict(X)
        accuracy = np.sum(Y_pred == Y) / len(Y)
        return accuracy
