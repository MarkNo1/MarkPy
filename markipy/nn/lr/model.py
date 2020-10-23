import torch
from torch import nn
from time import sleep
from tqdm import tqdm
import wandb

from markipy.nn.common import make_ramp, make_one

class LogisticRegrssion(nn.Module):
    def __init__(self, input):
        super(LogisticRegrssion, self).__init__()
        self.l1 = nn.Sequential(nn.Linear(input, 100),nn.Sigmoid())

    def forward(self, x):
        return self.l1(x)



if __name__ == "__main__":
    # DIMENSION 
    # Computational Device 
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    #Wb1. Start a new run
    wandb.init(project="lr")

    #Wb2. Save model inputs and hyperparameters
    config = wandb.config
    # Parameters
    config.learning_rate = lr = 0.001
    config.epoch = epoch = int(1e3)
    config.input_dimension = dim = 100

    # X Tensor 
    m = 100 ; n = 200 
    x = make_ramp(m,n)

    # Y Tensor
    tensor_y = make_one((m , 1), device=device).view(2, 1)

    # Init model
    model = LogisticRegrssion(1)

    #Wb3. Log gradients and model parameters
    wandb.watch(model)

    # Cost Function
    criterion = nn.BCELoss()

    # Optimizer
    optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

    # Tdqm
    bar = tqdm([x for x in range(epoch)], desc="Logistic Regrssion")

    # Optional
    model.train()

    # Loop for epoch 
    for iteration in bar:
        # Loop for batch 
        for index in x:
            optimizer.zero_grad()
            y_ = model(tensor_x[index % dim])
            loss = criterion(y_, tensor_y[index % 2])
            loss.backward()
            optimizer.step()

        wandb.log({"epoch": epoch, "loss": loss})
