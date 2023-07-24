import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

def d(x, y, t):
    
    if t == 'vector':
        distance = np.linalg.norm(x - y)
    elif t == 'matrix':
        row, col = y.shape
        distance = np.zeros((row, 1))
        for i in range(row):
           distance[i] = np.linalg.norm(x - y[i,:]) 

    return distance

# Hyper Parameters
C = 3
m = 1.1
iteration = 10

X = pd.read_csv('xclara.csv')
n, dimension = X.shape

U = np.array(np.random.rand(n, C), dtype='double')
U_crisp = np.zeros((n, 1))
mu = np.zeros((C, dimension))
X = np.array(X)
fig, ax = plt.subplots()

for k in range(iteration):
    
    for i in range(n):
        U[i,:] = U[i,:] / sum(U[i,:])

    for j in range(C):
        temp = (U[:,j] ** m)
        mu[j, :] = sum(np.multiply(temp,X.transpose()).transpose()) / sum(temp)
    
    for i in range(n):
        for j in range(C):
            U[i,j] = 1 / sum((d(X[i,:], mu[j,:], 'vector')) / d(X[i,:], mu[:,:], 'matrix')) ** (1 / (m-1))
            
    ax.scatter(X[:, 0], X[:, 1], s=1, c='#000000')
    ax.scatter(mu[:, 0], mu[:, 1], marker='*', s=200, c='#ffff00')
    plt.title('iteration ' + str(k), fontdict=None, loc='center', pad=None)
    plt.pause(0.01)
    ax.clear()

for i in range(n):
   U_crisp[i] = np.argmax(U[i,:])

colors = ['r', 'g', 'b', 'y', 'c', 'm']

for i in range(C):
    points = np.array([X[j, :] for j in range(n) if U_crisp[j] == i])
    #print(points)
    ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
    
ax.scatter(mu[:, 0], mu[:, 1], marker='*', s=200, c='#ffff00')
plt.show()