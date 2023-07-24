import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import wandb


# preparing dataset
data = pd.read_csv("weight-height.csv")
data = data.loc[np.r_[0:200, 5001:5201], :]
X = data["Height"].values
Y = data["Weight"].values
X = X.reshape(-1, 1)
Y = Y.reshape(-1, 1)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, shuffle=True)


# init params
wandb.init(project='weight height')
w = np.random.rand(1, 1)
b = np.random.rand(1, 1)


# hyper parameters
config = wandb.config
config.learning_rate_w = 0.0001
config.learning_rate_b = 0.1
config.epochs = 50


Errors = []
Errors_test = []
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)


# train
for epoch in range(config.epochs):
    for i in range(X_train.shape[0]):
        x = X_train[i]
        y = Y_train[i]

        y_pred = x * w + b
        e = y - y_pred

        # update SGD
        w += config.learning_rate_w * e * x
        b += config.learning_rate_b * e

    Y_pred = X_train * w + b
    ax1.clear()
    ax1.scatter(X_train, Y_train, c='green')
    ax1.plot(X_train, Y_pred, c='red')

    Error = np.mean(Y_train - Y_pred) ** 2
    Errors.append(Error) # MSE
    ax2.clear()
    ax2.plot(Errors)
    wandb.log({"Loss Train": Error})

    Y_pred = X_test * w + b
    Error_test = np.mean(Y_test - Y_pred) ** 2
    Errors_test.append(Error_test)
    ax3.clear()
    ax3.plot(Errors_test)
    wandb.log({"Loss test": Error_test})

    plt.pause(0.1)

plt.show()
