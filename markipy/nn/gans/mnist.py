import torch
from torch import nn
from tqdm.auto import tqdm
from torchvision import transforms
from torchvision.datasets import MNIST  # Training dataset
from torchvision.utils import make_grid
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
import wandb

from .gen import get_gen_loss, Generator
from .discriminator import get_disc_loss, Discriminator

torch.manual_seed(0)  # Set for testing purposes, please do not change!

PROJECT="MNIST"

if __name__ == "__main__":
    

    # Weights and Biases. Profiler
    # wandb.init(project=PROJECT)
    # config = wandb.config

    # Hyperparameters and Store
    config.criterion = criterion = nn.BCEWithLogitsLoss()
    config.n_epochs = n_epochs = 200
    config.z_dim = z_dim = 64
    config.display_step= display_step = 500
    config.batch_size = batch_size = 128
    config.lr = lr = 0.00001
    config.device = device = 'cuda'

    # Load MNIST dataset as tensors
    dataloader = DataLoader(
        MNIST('.', download=True, transform=transforms.ToTensor()),
        batch_size=batch_size,
        shuffle=True)

    gen = Generator(z_dim).to(device)
    gen_opt = torch.optim.Adam(gen.parameters(), lr=lr)
    disc = Discriminator().to(device)
    disc_opt = torch.optim.Adam(disc.parameters(), lr=lr)

    device = 'cuda'
    cur_step = 0
    mean_generator_loss = 0
    mean_discriminator_loss = 0
    test_generator = True  # Whether the generator should be tested
    gen_loss = False
    error = False
    for epoch in range(n_epochs):

        # Dataloader returns the batches
        for real, _ in tqdm(dataloader):
            cur_batch_size = len(real)

            # Flatten the batch of real images from the dataset
            real = real.view(cur_batch_size, -1).to(device)

            ### Update discriminator ###
            # Zero out the gradients before backpropagation
            disc_opt.zero_grad()

            # Calculate discriminator loss
            disc_loss = get_disc_loss(gen, disc, criterion, real, cur_batch_size, z_dim, device)

            # Update gradients
            disc_loss.backward(retain_graph=True)

            # Update optimizer
            disc_opt.step()

            # For testing purposes, to keep track of the generator weights
            if test_generator:
                old_generator_weights = gen.gen[0][0].weight.detach().clone()

            # Update gradients
            gen_opt.zero_grad()

            # Update optimizer
            gen_loss = get_gen_loss(gen, disc, criterion, cur_batch_size, z_dim, device)

            # Update gradients
            gen_loss.backward(retain_graph=True)

            # Update optimizer
            gen_opt.step()

            # For testing purposes, to check that your code changes the generator weights
            if test_generator:
                try:
                    assert lr > 0.0000002 or (gen.gen[0][0].weight.grad.abs().max() < 0.0005 and epoch == 0)
                    assert torch.any(gen.gen[0][0].weight.detach().clone() != old_generator_weights)
                except:
                    error = True
                    print("Runtime tests have failed")

            # Keep track of the average discriminator loss
            mean_discriminator_loss += disc_loss.item() / display_step

            # Keep track of the average generator loss
            mean_generator_loss += gen_loss.item() / display_step

            ### Visualization code ###
            if cur_step % display_step == 0 and cur_step > 0:
                print(
                    f"Epoch {epoch}, step {cur_step}: Generator loss: {mean_generator_loss}, discriminator loss: {mean_discriminator_loss}")
                fake_noise = get_noise(cur_batch_size, z_dim, device=device)
                fake = gen(fake_noise)
                show_tensor_images(fake)
                show_tensor_images(real)
                mean_generator_loss = 0
                mean_discriminator_loss = 0
            cur_step += 1
