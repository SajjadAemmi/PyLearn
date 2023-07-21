import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# Read data
data = np.array(pd.read_csv('linear_data_train.csv', skiprows=1, header=None))

X_train = np.matrix(data[:, 0:2])
Y_train = np.array(data[:, 2])

N = X_train.shape[0]

# Hyper parameters
lr = 0.001
epochs = 4

# Weights init
W = np.random.rand(2, 1)
b = np.random.rand(1, 1)

fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.view_init(15, 20)
        
x_range = np.arange(X_train[:,0].min(), X_train[:,0].max(), 0.1)
y_range = np.arange(X_train[:,1].min(), X_train[:,1].max(), 0.1)

errors = []
for i in range(epochs):
    for n in range(N):
        # print(n)
        y_pred = np.matmul(X_train[n], W) + b
        e = Y_train[n] - y_pred
        
        # update
        W += lr * X_train[n, :].T * e 
        b += lr * e

        # Error
        Y_pred = np.matmul(X_train, W) + b
        error = np.mean(Y_train - Y_pred)
        errors.append(error)
        print('error', error)

        # Plot Data
        ax.clear()
        x, y = np.meshgrid(x_range, y_range)
        z = x * W[0] + y * W[1] + b
        ax.plot_surface(x, y, z, rstride=1, cstride=1, alpha = 0.4)
        ax.scatter(X_train[Y_train == 1,0], X_train[Y_train == 1,1], Y_train[Y_train == 1], c='r', marker='o')
        ax.scatter(X_train[Y_train == -1,0], X_train[Y_train == -1,1], Y_train[Y_train == -1], c='g', marker='o')
        ax.set_xlabel('X0')
        ax.set_ylabel('X1')
        ax.set_zlabel('Y')
        plt.pause(0.001)

plt.show()
