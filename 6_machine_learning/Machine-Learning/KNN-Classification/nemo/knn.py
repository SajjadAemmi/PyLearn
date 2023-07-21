import numpy as np
from scipy.spatial.distance import cdist


class KNearestNeighbors:
    def __init__(self, k):
        self.k = k
    
    # train
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def nearNeighbors(self, X_test):
        point_dist = cdist(X_test, self.X_train)  # euclidianDistance
        neigh_ind = []
        for row in point_dist:
            near_neighbors = np.argsort(row)[:self.k]
            neigh_ind.append(near_neighbors)
        return np.array(neigh_ind)
    
    # test
    def predict(self, X_test):
        neighbors = self.nearNeighbors(X_test)
        y_pred = []
        for neighbor in neighbors:
            y_pred.append(np.argmax(np.bincount(self.y_train[neighbor])))
        return np.array(y_pred)
    
    def evaluate(self, X_test, y_test):
        y_pred = self.predict(X_test)
        evaluatation = (y_pred == y_test).sum() / len(y_test)
        return evaluatation
