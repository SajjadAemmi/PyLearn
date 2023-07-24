import argparse
import pandas as pd
import numpy as np
import torch
from tqdm import tqdm

from src.model import Model


def load_dataset():
    data = pd.read_csv(args.dataset)
    Y = data[['direction']]
    X = data[['w0', 'w1', 'w2', 'w3',
            'a0', 'a01', 'a1', 'a12', 'a2', 'a23', 'a3', 'a30',
            'b0', 'b01', 'b1', 'b12', 'b2', 'b23', 'b3', 'b30']]

    X = np.array(X, dtype=np.float32)
    Y = np.array(Y).flatten()

    X = torch.tensor(X)
    Y = torch.LongTensor(Y)
    return X, Y


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Snake AI')
    parser.add_argument("--dataset", default="./snake_train_dataset.csv", help="dataset path", type=str)
    parser.add_argument("--epochs", default=8, help="number of epochs", type=int)
    parser.add_argument("--lr", default=1e-4, help="learning rate", type=float)
    parser.add_argument("--batch-size", default=64, help="batch size", type=int)
    parser.add_argument("--weights", default="./weights/snake.pt", help="weights path", type=str)
    args = parser.parse_args()

    X, Y = load_dataset()
    args = parser.parse_args()

    X, Y = load_dataset()
    N = X.shape[0]
    train_dataset = torch.utils.data.TensorDataset(X, Y)
    train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=args.batch_size, shuffle=True)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    model = Model()
    model = model.to(device)

    loss_fn = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)

    model.train()
    for epoch in range(1, args.epochs + 1):
        correct = 0
        for batch_idx, (data, target) in tqdm(enumerate(train_loader), position=0, leave=True):
            data = data.to(device) 
            target = target.to(device)
        
            optimizer.zero_grad()
            output = model(data)
        
            loss = loss_fn(output, target)
            loss.backward()
            optimizer.step()

            correct += (output.argmax(dim=1) == target).float().sum()

        accuracy = 100 * correct / N
        print(f"Epoch: {epoch}\tLoss: {loss.item():.6f}\tAccuracy: {accuracy:.6f}")

    torch.save(model.state_dict(), args.weights)
