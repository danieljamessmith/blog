import matplotlib.pyplot as plt
from torchvision.datasets import FashionMNIST
from torchvision import transforms
from torch.utils.data import DataLoader
import numpy as np
import prettytable
import sys
import torch
import torchvision
import pytorch_lightning as pl

def versions():
    table = prettytable.PrettyTable()
    table.field_names = ["Component", "Version"]
    table.add_row(["Python", sys.version.split(' ')[0]])
    table.add_row(["PyTorch", torch.__version__])
    table.add_row(["PyTorch Lightning", pl.__version__])
    table.add_row(["torchvision", torchvision.__version__])
    table.hrules = prettytable.ALL
    print(table)

def show_img():
    # Load FashionMNIST dataset
    transform = transforms.Compose([transforms.ToTensor()])
    fashion_mnist = FashionMNIST(root='./data', train=True, download=True, transform=transform)
    loader = DataLoader(fashion_mnist, batch_size=4, shuffle=True)

    # Get one batch of four images
    dataiter = iter(loader)
    images, labels = next(dataiter)

    # Class labels for Fashion-MNIST
    classes = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    # Create a grid of subplots
    fig, axes = plt.subplots(2, 2, figsize=(8, 8))
    axes = axes.ravel()

    for idx in range(4):
        axes[idx].imshow(images[idx].squeeze(), cmap='gray')  # Squeeze removes single-dimensional entries from the shape
        axes[idx].set_title(classes[labels[idx]])
        axes[idx].axis('off')

    plt.tight_layout()
    plt.show()

