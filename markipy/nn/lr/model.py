import torch
from torch import nn
from time import sleep
from tqdm import tqdm
import wandb


class LogisticRegrssion(nn.Module):
    def __init__(self, input):
        super(LogisticRegrssion, self).__init__()
        self.l1 = nn.Linear(input, 100)
        self.l2 = nn.Linear(100, 1)
        self.rel = nn.ReLU()
        self.sig = nn.Sigmoid()

    def forward(self, x):
        x = self.rel(self.l1(x))
        return  self.sig(self.l2(x))


if __name__ == "__main__":
    # 1. Start a new run
    wandb.init(project="lr")

    # 2. Save model inputs and hyperparameters
    config = wandb.config
    config.learning_rate = 0.001

    epoch = int(1e3)
    dim = 100

    x = [x for x in range(dim)]
    y = torch.FloatTensor([0, 1])

    tensor_x = torch.FloatTensor(x).view(dim, 1)
    tensor_y = torch.FloatTensor(y).view(2, 1)

    # Init model
    model = LogisticRegrssion(1)

    # 3. Log gradients and model parameters
    wandb.watch(model)

    # Cost Function
    criterion = nn.BCELoss()

    # Optimizer
    optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

    bar = tqdm([x for x in range(epoch)], desc="Logistic Regrssion")

    model.train()

    for iteration in bar:
        for index in x:
            optimizer.zero_grad()
            y_ = model(tensor_x[index % dim])
            loss = criterion(y_, tensor_y[index % 2])
            loss.backward()
            optimizer.step()
        wandb.log({"epoch": epoch, "loss": loss})
