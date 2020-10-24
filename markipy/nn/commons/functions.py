from torchvision.utils import make_grid
import matplotlib.pyplot as plt
import torch


def show_tensor_images(image_tensor, num_images=25, size=(1, 28, 28)):
    """
    Function for visualizing images: Given a tensor of images, number of images, and
    size per image, plots and prints the images in a uniform grid.
    """
    image_unflat = image_tensor.detach().cpu().view(-1, *size)
    image_grid = make_grid(image_unflat[:num_images], nrow=5)
    plt.imshow(image_grid.permute(1, 2, 0).squeeze())
    plt.show()


def make_noise(n_samples, dimensions, device='cuda'):
    """
    Function for creating noise vectors: Given the dimensions (n_samples, z_dim),
    creates a tensor of that shape filled with random numbers from the normal distribution.
    Parameters:
        n_samples: the number of samples to generate, a scalar
        dimensions: the dimension of the noise vector, a scalar
        device: the device type
    """
    # NOTE: To use this on GPU with device='cuda', make sure to pass the device
    # argument to the function you use to generate the noise.
    return torch.randn(n_samples, dimensions, device=device)


def make_one(size=(1, 1), device=torch.device('cuda')):
    return torch.ones(size=size, device=device)


def make_ramp(size=(1, 1), device=torch.device('cuda')):
    X = torch.ones(size=size, device=device)
    i = 0
    for x in X:
        x += i
        i += 1
    return X



