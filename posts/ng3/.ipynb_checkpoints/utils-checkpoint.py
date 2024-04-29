import math
import numpy as np
import pandas as pd
import h5py
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import tensorflow as tf
from tensorflow.python.framework import ops
import prettytable
import sys

def versions():
    table = prettytable.PrettyTable()
    table.field_names = ["Component", "Version"]
    table.add_row(["Python", sys.version.split(' ')[0]])
    table.add_row(["TensorFlow", tf.__version__])
    table.hrules = prettytable.ALL
    print(table)


def load_dataset():
    train_dataset = h5py.File('datasets/train_signs.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # your train set labels

    test_dataset = h5py.File('datasets/test_signs.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) # your test set labels

    classes = np.array(test_dataset["list_classes"][:]) # the list of classes
    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes




def convert_to_one_hot(Y, C):
    Y = np.eye(C)[Y.reshape(-1)].T
    return Y



def plot_model_history(history, epochs=20):
    """
    Plots the training and validation loss and accuracy of a trained model.

    Parameters:
    history (History): The history object of a trained model.

    Returns:
    None
    """
    # Convert the history.history dict to a pandas DataFrame
    df_history = pd.DataFrame(history.history)
    df_history.index += 1

    # Rename the columns
    df_loss = df_history[['loss', 'val_loss']].rename(columns={'loss': 'Train', 'val_loss': 'Validation'})
    df_acc = df_history[['accuracy', 'val_accuracy']].rename(columns={'accuracy': 'Train', 'val_accuracy': 'Validation'})

    # Set the style of seaborn
    sns.set(style="whitegrid")

    # Create subplots
    fig, axs = plt.subplots(1, 2, figsize=(20, 8))

    # Plot loss
    loss_plot = sns.lineplot(data=df_loss, ax=axs[0])
    axs[0].set(xlabel='Epoch', ylabel='Loss')
    axs[0].set_title('Loss', fontsize=20)
    axs[0].xaxis.set_major_locator(ticker.MultipleLocator(int(epochs/20)))
    axs[0].yaxis.set_major_locator(ticker.MultipleLocator(0.1))  
    axs[0].set_xlim([1, epochs]) 
    axs[0].set_ylim([0, None])
    loss_plot.legend(loc='upper right')
    
    # Plot accuracy
    acc_plot = sns.lineplot(data=df_acc, ax=axs[1])
    axs[1].set(xlabel='Epoch', ylabel='Accuracy (%)')
    axs[1].set_title('Accuracy', fontsize=20)
    axs[1].xaxis.set_major_locator(ticker.MultipleLocator(int(epochs/20)))  
    axs[1].yaxis.set_major_formatter(ticker.PercentFormatter(1.0))  # Format y-axis labels as percentages
    axs[1].yaxis.set_major_locator(ticker.MultipleLocator(0.1))  
    axs[1].set_xlim([1, epochs]) 
    axs[1].set_ylim([0, 1]) 
    acc_plot.legend(loc='upper left')

    plt.tight_layout()
    plt.subplots_adjust(wspace=0.15)
    plt.show()



def print_mislabeled_images(classes, X, y, p, number):
    """
    Plots images where predictions and truth were different.
    X -- dataset
    y -- true labels
    p -- predictions
    number -- number of mislabeled images to display
    """
    mislabeled_indices = np.asarray(np.where(p != y))
    mislabeled_indices = mislabeled_indices[1]  # Select the indices of mislabeled images
    plt.rcParams['figure.figsize'] = (40.0, 40.0) # set default size of plots
    num_images = len(mislabeled_indices)
    
    # If there are more mislabeled images than the specified number, 
    # randomly select a subset of the mislabeled images without replacement

    mislabeled_indices = np.random.choice(mislabeled_indices, size=number, replace=False)
    num_images = number
    
    for i in range(num_images):
        index = mislabeled_indices[i]
        
        plt.subplot(2, num_images, i + 1)
        plt.imshow(X[index].reshape(64,64,3), interpolation='nearest')
        plt.axis('off')
        plt.title("Prediction: " + str(classes[int(p[index])]) + " \n Class: " + str(classes[y[0,index]]))
    plt.show()




