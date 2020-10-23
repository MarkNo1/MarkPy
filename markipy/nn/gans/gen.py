import torch
from torch import nn


def get_generator_block(input_dim, output_dim):
    """
    Function for returning a block of the generator's neural network
    given input and output dimensions.
    Parameters:
        input_dim: the dimension of the input vector, a scalar
        output_dim: the dimension of the output vector, a scalar
    Returns:
        a generator neural network layer, with a linear transformation
          followed by a batch normalization and then a relu activation
    """
    return nn.Sequential(
        nn.Linear(input_dim, output_dim),
        nn.BatchNorm1d(output_dim),
        nn.ReLU(inplace=True),
    )


# def get_piramide_block(dimension, ):


class Mask(nn.Module):
    def __init__(self, *dims):
        super(Mask, self).__init__()
        self.dimension = torch.Size([dims])
        self.weight = self.get_new_mask_weight()
        self.weight.data.uniform_(0.88, 0.99)

    def forward(self, x):
        x_dims = x.s
        x_1d = torch.flatten(x)
        # To-Do
        # Flatt to 2D
        # MatMul
        # Unflat
        return self.weight.mul(x)

    def get_new_mask_weight(self, requires_grad=True):
        return torch.nn.Parameter(data=torch.Tensor(self.dimension), requires_grad=requires_grad)


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.Mask = Mask(100)

    def forward(self, x):
        x = Mask(x)
        return x


def AutoRetroActionEncoder(input_dim, output_dim=0, scale=1, load=0):
    if output_dim == 0:
        # Calculate the correct scale for the parameters

        scaled = 1
        output_dim = scaled


    return nn.Sequential(nn.ConvTranspose2d())


class Generator(nn.Module):
    """
    Generator Class
    Values:
        z_dim: the dimension of the noise vector, a scalar
        im_dim: the dimension of the images, fitted for the dataset used, a scalar
          (MNIST images are 28 x 28 = 784 so that is your default)
        hidden_dim: the inner dimension, a scalar
    """

    def __init__(self, dimension=10, im_dim=784, hidden_dim=128):
        super(Generator, self).__init__()
        # Build the neural network
        self.wandb = nn.Sequential(
            get_generator_block(dimension, hidden_dim),
            get_generator_block(hidden_dim, hidden_dim * 2),
            get_generator_block(hidden_dim * 2, hidden_dim * 4),
            get_generator_block(hidden_dim * 4, hidden_dim * 8),
            nn.Linear(hidden_dim * 8, im_dim),
            nn.Sigmoid(),
        )

    def forward(self, noise):
        """
        Function for completing a forward pass of the generator: Given a noise tensor,
        returns generated data.
        Parameters:
            noise: a noise tensor with dimensions (examples, dimensions)
        """
        return self.layer(noise)

    # Needed for grading
    def get_layer(self):
        return self.wandb


if __name__ == '__main__':

    model = Model()

    for name, param in model.named_parameters():
        print(name, param)
