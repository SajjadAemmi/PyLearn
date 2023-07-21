import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# Read data
data = np.array(pd.read_csv('linear_data_train.csv', skiprows=1, header=None))

X_train = np.matrix(data[:, 0:2])
Y_train = np.array(data[:, 2])

N = X_train.shape[0]

# Hyper parameters
lr = 0.01
epochs = 2

# Weights init
W = np.random.rand(2, 1)
b = np.random.rand(1, 1)

fig1, (ax1, ax2) = plt.subplots(1, 2)

errors = []
for i in range(epochs):
    
    for n in range(N):
        y_pred = np.matmul(X_train[n], W) + b
        e = Y_train[n] - y_pred
        
        # update
        W += lr * X_train[n, :].T * e * 2
        b += lr * e

        # Error
        Y_pred = np.matmul(X_train, W) + b
        error = np.mean(np.square(Y_train - Y_pred))
        errors.append(error)

        # Plot Data
        ax1.clear()
        x = range(0, 2)
        YY = -(x * W[0] + b) / W[1]
        ax1.plot(x, YY.T, '-g', lw=1)
        
        ax1.scatter([X_train[Y_train == -1,0]], [X_train[Y_train == -1,1]], c='r', marker='x')
        ax1.scatter([X_train[Y_train == 1,0]], [X_train[Y_train == 1,1]], c='b', marker='o')
  
        # Plot Error
        ax2.clear()
        ax2.set_title('Loss')
        ax2.plot(errors, '-b', lw=1)

        plt.pause(0.001)

plt.show()
