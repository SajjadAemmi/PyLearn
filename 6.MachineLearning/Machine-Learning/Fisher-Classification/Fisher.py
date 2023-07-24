import numpy as np
import numpy.matlib
import pandas as pd
from matplotlib import pyplot as plt

# Set Data
X1 = np.random.randn(200,2) * 2
X2 = (np.random.randn(200,2) + [6, -6]) * 2
X = np.concatenate((X1, X2), axis=0)

Y1 = np.matlib.repmat(-1,200,1)
Y2 = np.matlib.repmat(1,200,1)
Y = np.concatenate((Y1, Y2), axis=0)

# Process Data
m1 = np.mean(X1, axis=0)
m2 = np.mean(X2, axis=0)
         
cov1 = np.cov(X1.T)
cov2 = np.cov(X2.T)

Sw = cov1 + cov2

Sw_inv = np.linalg.inv(Sw);

w = np.matmul(Sw_inv, (m1 - m2))

mu1 = np.matmul(m1, w)
mu2 = np.matmul(m2, w)

b = (mu1 + mu2) / 2

x = [i for i in range(-20,20)]

y1 = np.multiply(x , w[1]) / w[0]
y2 = -(np.multiply(x , w[0]) - b) / w[1]  

# Plot
plt.xlim(-10, 20)
plt.ylim(-20, 10)

plt.scatter(X1[:,0], X1[:,1], s=1, c='#ff0000')
plt.scatter(X2[:,0], X2[:,1], s=1, c='#0000ff')

plt.scatter(m1[0], m1[1], s=20, c='#ff0000')
plt.scatter(m2[0], m2[1], s=20, c='#0000ff')

plt.plot(x, y1, c='#00ff00')     
plt.plot(x, y2, c='#ff00ff')
plt.show()