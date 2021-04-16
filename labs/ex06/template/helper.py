from math import inf

import matplotlib
import numpy as np
import sklearn.datasets
import torch
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from torch.utils import data

import sys, os
SEED = 0

# Disable printing while visualization
def disable_print():
    sys.stdout = open(os.devnull, 'w')

# Restore printing
def enable_print():
    sys.stdout = sys.__stdout__
    
def generate_dataset(name, n_samples=200):
    """
    Generate a random dataset with any of the predefined structures
    `blobs`, `moons`, `circles`, `bar`, or `xor`
    """
    # Use Scikit-Learn's make_* functions to generate the samples
    if name == "blobs":
        coordinates, labels = sklearn.datasets.make_blobs(n_samples=n_samples, centers=2, random_state = SEED)
    elif name == "moons":
        coordinates, labels = sklearn.datasets.make_moons(n_samples=n_samples, random_state = SEED)
        coordinates[labels == 1] += 0.1
        coordinates[labels == 0] -= 0.1
    elif name == "circles":
        coordinates, labels = sklearn.datasets.make_circles(n_samples=n_samples, random_state = SEED)
        coordinates[labels == 1] *= 0.5
    elif name == "bar":
        # coordinates = np.random.rand(n_samples, 2) * 2 - 1  # range -1 to 1

        x_coordinate, y_coordinate = np.meshgrid(
            np.linspace(-1, 1, 12, dtype=np.float32),
            np.linspace(-1, 1, 6, dtype=np.float32),
        )
        coordinates = np.stack([x_coordinate.reshape(-1), y_coordinate.reshape(-1)], axis=-1)
        n_samples = len(coordinates)

        l1norm = np.linalg.norm(coordinates, ord=inf, axis=1)
        labels = np.ones_like(l1norm).astype(np.int64)
        labels[np.abs(coordinates[:, 0]) < 0.1] = 0
    elif name == "xor":
        np.random.seed(SEED)
        coordinates = np.random.rand(n_samples, 2)

        # Create a small gap between the classes
        gap_size = 0
        coordinates[coordinates[:, 0] > 0.5, 0] += gap_size * 0.5
        coordinates[coordinates[:, 0] < 0.5, 0] -= gap_size * 0.5
        coordinates[coordinates[:, 1] > 0.5, 1] += gap_size * 0.5
        coordinates[coordinates[:, 1] < 0.5, 1] -= gap_size * 0.5

        labels = np.logical_xor(coordinates[:, 0] > 0.5, coordinates[:, 1] > 0.5).astype(np.int64)
        noisy_index = np.where(np.random.binomial(1, 0.1, size = len(coordinates)))[0]
        coordinates[noisy_index] += np.random.laplace(0, 0.1, [len(noisy_index), 2])

    else:
        raise ValueError("Unknown dataset name {}".format(name))

    # Convert to PyTorch
    coordinates = coordinates.astype(np.float32)
    coordinates = torch.from_numpy(coordinates)
    labels = torch.from_numpy(labels)

    # Normalize the range of coordinates to be 0 to 1
    coordinates -= torch.min(coordinates, 0, keepdim=True)[0]
    coordinates /= torch.max(coordinates, 0, keepdim=True)[0]

    # Create a PyTorch dataset
    dataset = data.TensorDataset(coordinates, labels)

    # Split it 50/50 into train and test
    train, test = torch.utils.data.random_split(dataset, [n_samples // 2, n_samples // 2])
    return train, test

def visualize_one_dataset(dataset: data.Dataset, ax: matplotlib.axes.Axes):
    for coordinate, label in dataset:
        x, y = coordinate
        color = {0: "#bada55", 1: "#55bada"}[label.item()]
        marker = {0: "+", 1: "."}[label.item()]
        ax.scatter(x, y, c=color, marker=marker)


def visualize_datasets(datasets):
    f, axes = plt.subplots(2, len(datasets))
    f.set_figheight(7)
    f.set_figwidth(14)
    axes[0][0].set_ylabel("Training")
    axes[1][0].set_ylabel("Test")
    for i, (name, train_set, test_set) in enumerate(datasets):
        visualize_one_dataset(train_set, ax=axes[0][i])
        visualize_one_dataset(test_set, ax=axes[1][i])
        axes[0][i].set_title(name)
    plt.show()

#%% Visualize the predictions of a model on a grid
def predict_grid(model, ax, xmin=-0.1, xmax=1.1, ymin=-0.1, ymax=1.1, num_grid_points=40):
    x_coordinate, y_coordinate = np.meshgrid(
        np.linspace(xmin, xmax, num_grid_points, dtype=np.float32),
        np.linspace(ymin, ymax, num_grid_points, dtype=np.float32),
    )
    x_coordinate = torch.from_numpy(x_coordinate)
    y_coordinate = torch.from_numpy(y_coordinate)
    coordinates = torch.stack([x_coordinate.view(-1), y_coordinate.view(-1)], dim=-1)
    predictions = torch.nn.functional.softmax(model(coordinates), dim=1)[:, 1]

    predictions = predictions.view(*x_coordinate.shape).detach()
    cmap = LinearSegmentedColormap.from_list("bada55_dark", ["#4d5b23", "#234d5b"], N=100)
    ax.pcolormesh(x_coordinate, y_coordinate, predictions, cmap=cmap)    

def visualize_predictions(datasets, model, optimize):
    f, axes = plt.subplots(3, len(datasets))
    f.set_figheight(10)
    f.set_figwidth(14)
    axes[0][0].set_ylabel("Training")
    axes[1][0].set_ylabel("Test")
    axes[2][0].set_ylabel("Test Loss")
    for i, (name, train_set, test_set) in enumerate(datasets):        
        axes[0][i].set_title(name + ' (%s)'% model.name)
        # train model
        model.init_params(train_set)
        disable_print()
        losses = optimize(train_set, test_set, model)
        enable_print()
        #plot results
        predict_grid(model, ax=axes[1][i])
        visualize_one_dataset(train_set, ax=axes[0][i])
        visualize_one_dataset(test_set, ax=axes[1][i])
        axes[2][i].plot(losses)
        axes[2][i].set_ylim([0,1])
    plt.show()