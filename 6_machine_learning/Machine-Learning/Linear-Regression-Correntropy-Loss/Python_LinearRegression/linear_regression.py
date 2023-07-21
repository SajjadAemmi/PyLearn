import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


# Read data
X = np.array(pd.read_csv('regressionOutliers.csv', skiprows = 1, header = None))

Y = np.array(X[:,1])
X[:,1] = 1
n, d = X.shape
Y = Y.reshape(n, 1)

# Correntropy loss function

# Hyper parameters
η = 0.1
iteration = 50

# Weights init
W = np.random.rand(d,1)
fig, ax1 = plt.subplots()

for k in range(iteration):
    
    e = Y - np.matmul(X, W)
    μ = np.exp(-η * e ** 2)
    
    R = np.matmul(X.T , X * μ)
    P = np.matmul(X.T , Y * μ)
    W = np.matmul(np.linalg.inv(R), P)
   
    Y_hat = np.matmul(X, W)
    
    # Plot
    
    plt.scatter(X[:, 0], Y[:, 0], s=1, c='#ff0000')
    ax1.plot(X[:, 0], Y_hat, '-c', lw=1)
    plt.pause(0.1)
    ax1.clear()
    
plt.scatter(X[:, 0], Y, s=1, c='#ff0000')
ax1.plot(X[:, 0], Y_hat, '-b', lw=3)    
plt.show()

# Square loss function + Regularization term

# Hyper parameters
λ = 3

R = np.matmul(X.T, X)
Rr = R + λ * np.eye(2)
P = np.matmul(X.T, Y)
W = np.matmul(np.linalg.inv(Rr), P)
Y_hat = np.matmul(X, W)
    
# Plot
plt.plot(X[:, 0], Y_hat,'-g', lw=3)