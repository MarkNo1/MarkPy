import torch
from torch import nn
from time import sleep
from tqdm import tqdm
from datetime import datetime

# import wandb

from markipy.nn.commons import make_ramp, make_one

class LogisticRegrssion(nn.Module):
    def __init__(self, input):
        super(LogisticRegrssion, self).__init__()
        self.l1 = nn.Sequential(nn.Linear(1, 100), nn.LeakyReLU(negative_slope=0.2), nn.Linear(100, 1),nn.Sigmoid())

    def forward(self, x):
        return self.l1(x)



if __name__ == "__main__":

    #Wb1. Start a new run
    # wandb.init(project="lr")

    #Wb2. Save model inputs and hyperparameters
    # config = wandb.config
    # # Parameters
    # config.learning_rate = 
    # config.epoch = epoch = int(1e3)
    # config.input_dimension = dim = 100



    # 1D
    dim = 100 
    lr = 0.1e-3
    epoch = int(1e6)

    # X Tensor 
    x = torch.ones(size=(dim,1), device='cuda')
    for i in range(len(x)):
        x[i] = x[i] * i



    # Y Tensor
    y = torch.ones(size=(dim,1), device='cuda')
    for i in range(len(y)):
        y[i] = i % 2 
    



    # Init model
    model = LogisticRegrssion(dim)

    #Wb3. Log gradients and model parameters
    # wandb.watch(model)

    # Cost Function
    criterion = nn.BCELoss()

    # Optimizer
    optimizer = torch.optim.SGD(model.parameters(), lr=lr)

    # Tdqm
    bar = tqdm(range(epoch), total=epoch, desc="Discovery run: {datatime.date()}")

    # Optional
    # model.train()
    model = model.cuda()

    # Loop for epoch 
    batch_size = 1
    for epoc in range(epoch):
        # Loop x 
        optimizer.zero_grad()
        y_ = model( x )
        loss = criterion(y_, y)
        loss.backward()
        optimizer.step()

        # print(f"epoch:{epoc} loss:{loss.item()} : ")
        bar.set_description(f"epoch:{epoc} loss:{loss.item()}")

        # wandb.log({"epoch": epoch, "loss": loss})
