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
        return self.sig(self.l2(x))


if __name__ == "__main__":
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

    # Data Input X and Y
    x = [x for x in range(dim)]
    y = torch.FloatTensor([0, 1]).cuda()

    # Pytorch Tensor
    tensor_x = torch.FloatTensor(x).view(dim, 1)
    tensor_y = torch.FloatTensor(y).view(2, 1).cuda()
    
    # (CUda) Check  
    tensor_x = tensor_x.to_device(device)
    tensor_x = tensor_y.to_device(device)

    # Init model
    model = LogisticRegrssion(1).cuda()

    #Wb3. Log gradients and model parameters
    wandb.watch(model)

    # Cost Function
    criterion = nn.BCELoss().cuda()

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
