import torch
from torch import nn
from torchvision.utils import make_grid
from torchvision import transforms
from torchvision.datasets import MNIST
from torch.utils.data import DataLoader
import torch.nn.functional as F
import matplotlib.pyplot as plt

from markipy import makedirs
from markipy.nn import DEFAULT_DATA_PATH


def show_tensor_images(image_tensor, num_images=25, size=(1, 28, 28), filename=None, nrow=5):
    '''
    Function for visualizing images: Given a tensor of images, number of images, and
    size per image, plots and prints the images in an uniform grid.
    '''
    image_tensor = (image_tensor + 1) / 2
    image_unflat = image_tensor.detach().cpu()
    image_grid = make_grid(image_unflat[:num_images], nrow=nrow)
    plt.imshow(image_grid.permute(1, 2, 0).squeeze())
    if filename is not None:
        # Image results
        images_path = '/tmp/coursera/mnist/week4/'
        makedirs(images_path, exist_ok=True)
        plt.savefig(filename, format='jpg')
    else:
        plt.show()


def make_grad_hook():
    '''
    Function to keep track of gradients for visualization purposes,
    which fills the grads list when using model.apply(grad_hook).
    '''
    grads = []

    def grad_hook(m):
        if isinstance(m, nn.Conv2d) or isinstance(m, nn.ConvTranspose2d):
            grads.append(m.weight.grad)

    return grads, grad_hook


def get_one_hot_labels(labels, n_classes):
    '''
    Function for creating one-hot vectors for the labels, returns a tensor of shape (?, num_classes).
    Parameters:
        labels: tensor of labels from the dataloader, size (?)
        n_classes: the total number of classes in the dataset, an integer scalar
    '''
    return F.one_hot(labels, n_classes)


def combine_vectors(x, y):
    '''
    Function for combining two vectors with shapes (n_samples, ?) and (n_samples, ?).
    Parameters:
      x: (n_samples, ?) the first vector.
        In this assignment, this will be the noise vector of shape (n_samples, z_dim),
        but you shouldn't need to know the second dimension's size.
      y: (n_samples, ?) the second vector.
        Once again, in this assignment this will be the one-hot class vector
        with the shape (n_samples, n_classes), but you shouldn't assume this in your code.
    '''
    # Note: Make sure this function outputs a float no matter what inputs it receives
    combined = torch.cat((x.float(), y.float()), 1)
    return combined


def get_MNIST_dataloader(batch_size=32):
    # You can tranform the image values to be between -1 and 1 (the range of the tanh activation)
    transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,)),
    ])
    return DataLoader(
        MNIST(DEFAULT_DATA_PATH / 'MNIST', download=True, transform=transform),
        batch_size=batch_size,
        pin_memory=True,
        shuffle=True)


# def interpolate_class(first_number, second_number, n_interpolation):
#     interpolation_noise = get_noise(n_view, z_dim, device=device).repeat(n_interpolation, 1)
#     first_label = get_one_hot_labels(torch.Tensor([first_number]).long(), n_classes)
#     second_label = get_one_hot_labels(torch.Tensor([second_number]).long(), n_classes)
#
#     # Calculate the interpolation vector between the two labels
#     percent_second_label = torch.linspace(0, 1, n_interpolation)[:, None]
#     interpolation_labels = first_label * (1 - percent_second_label) + second_label * percent_second_label
#
#     # Combine the noise and the labels
#     noise_and_labels = combine_vectors(interpolation_noise, interpolation_labels.to(device))
#     fake = gen(noise_and_labels)
#     show_tensor_images(fake, num_images=n_interpolation, nrow=int(math.sqrt(n_interpolation)), show=False)
#
#
#
# def interpolate_noise(first_noise, second_noise):
#     # This time you're interpolating between the noise instead of the labels
#     percent_first_noise = torch.linspace(0, 1, n_interpolation)[:, None].to(device)
#     interpolation_noise = first_noise * percent_first_noise + second_noise * (1 - percent_first_noise)
#
#     # Combine the noise and the labels again
#     noise_and_labels = combine_vectors(interpolation_noise, interpolation_label.to(device))
#     fake = gen(noise_and_labels)
#     show_tensor_images(fake, num_images=n_interpolation, nrow=int(math.sqrt(n_interpolation)), show=False)


def calculate_updated_noise(noise, weight):
    '''
    Function to return noise vectors updated with stochastic gradient ascent.
    Parameters:
        noise: the current noise vectors. You have already called the backwards function on the target class
          so you can access the gradient of the output class with respect to the noise by using noise.grad
        weight: the scalar amount by which you should weight the noise gradient
    '''
    #### START CODE HERE ####
    new_noise = noise + (noise.grad * weight)
    #### END CODE HERE ####
    return new_noise


def get_score(current_classifications, original_classifications, target_indices, other_indices, penalty_weight):
    '''
    Function to return the score of the current classifications, penalizing changes
    to other classes with an L2 norm.
    Parameters:
        current_classifications: the classifications associated with the current noise
        original_classifications: the classifications associated with the original noise
        target_indices: the index of the target class
        other_indices: the indices of the other classes
        penalty_weight: the amount that the penalty should be weighted in the overall score
    '''
    # Steps: 1) Calculate the change between the original and current classifications (as a tensor)
    #           by indexing into the other_indices you're trying to preserve, like in x[:, features].
    #        2) Calculate the norm (magnitude) of changes per example.
    #        3) Multiply the mean of the example norms by the penalty weight.
    #           This will be your other_class_penalty.
    #           Make sure to negate the value since it's a penalty!
    #        4) Take the mean of the current classifications for the target feature over all the examples.
    #           This mean will be your target_score.
    #### START CODE HERE ####
    # Calculate the norm (magnitude) of changes per example and multiply by penalty weight
    other_class_penalty = - (
                original_classifications[:, other_indices] - current_classifications[:, other_indices]).norm(dim=1)
    # Take the mean of the current classifications for the target feature
    target_score = (current_classifications[:, target_indices]).mean() + other_class_penalty.mean() * penalty_weight
    #### END CODE HERE ####
    return target_score
