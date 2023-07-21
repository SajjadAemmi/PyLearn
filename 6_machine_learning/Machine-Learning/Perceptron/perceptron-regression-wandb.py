import numpy as np
from matplotlib import pyplot as plt
import wandb

    
def data_generator(N):
    X = np.random.uniform(0, 4, N)
    Y = X * 2 + np.random.normal(0, 0.5, N) + 1.5

    X = X.reshape(-1, 1)
    Y = Y.reshape(-1, 1)
    print(X.shape)
    print(Y.shape)
    return X, Y


wandb.init(project='gpt3', entity='sajjadaemmi')
config = wandb.config

N = 200
X_train, Y_train = data_generator(N)

# Hyper parameters
config.learning_rate = 0.0001
epochs = 4

# Weights init
W = np.random.rand(1, 1)
b = np.random.rand(1, 1)

fig1, (ax1, ax2) = plt.subplots(1, 2)

losses = []
for i in range(epochs):
    for n in range(N):
        y_pred = np.matmul(X_train[n], W) + b
        e = Y_train[n] - y_pred

        # update
        W += config.learning_rate * e * X_train[n]
        b += config.learning_rate * e

        # Error
        Y_pred = np.matmul(X_train, W) + b
        loss = np.mean(Y_train - Y_pred)
        losses.append(loss)
        wandb.log({"loss": loss})

        # Plot Data
        ax1.clear()
        ax1.set_title('Data')
        ax1.scatter(X_train, Y_train, s=1, c='#ff0000')
        ax1.plot(X_train, Y_pred, '-c', lw=2)
        plt.ylim(bottom=-1)

        # Plot Error
        ax2.clear()
        ax2.set_title('Loss')
        ax2.plot(losses, '-b', lw=1)

        plt.pause(0.01)

plt.show()
