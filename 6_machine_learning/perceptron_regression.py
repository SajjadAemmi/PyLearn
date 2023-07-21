import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

# Prepare Dataset
data = pd.read_csv("weight-height.csv")
data = data.loc[np.r_[0:200, 5001:5201], :]

X = data["Height"].values
Y = data["Weight"].values
# Y = data["Gender"].replace(["Male", "Female"], [1, 0]).values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y)

X_train = X_train.reshape(-1, 1)
Y_train = Y_train.reshape(-1, 1)

# Init
W = np.random.rand(1, 1)
b = np.random.rand(1, 1)

# Hyper parameters
η1 = 0.0001
η2 = 0.1
epochs = 30

Errors = []
fig, (ax1, ax2) = plt.subplots(1, 2)

# Train
for epoch in range(epochs):
    for i in range(X_train.shape[0]):
        x = X_train[i]
        y = Y_train[i]

        y_pred = x * W + b
        e = y - y_pred  # calc error

        W += η1 * e * x  # update
        b += η2 * e
        # print(b)

    Y_pred = X_train * W + b
    # Show Data
    ax1.clear()
    ax1.scatter(X_train, Y_train, c='blue')
    ax1.plot(X_train, Y_pred, c='red')
    # ax1.axis(ymin=0)
    # ax1.axis(xmin=0)

    # Show Loss
    Error = np.mean((Y_train - Y_pred) ** 2)
    Errors.append(Error)
    ax2.clear()
    ax2.plot(Errors)
    plt.pause(0.01)


# plt.scatter(X_train, Y_train)
# plt.ylim(bottom=0)
plt.show()