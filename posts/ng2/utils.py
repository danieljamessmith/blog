import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import h5py

def load_data():
    train_dataset = h5py.File('datasets/train_catvnoncat.h5', "r")
    train_set_x_orig = np.array(train_dataset["train_set_x"][:]) # your train set features
    train_set_y_orig = np.array(train_dataset["train_set_y"][:]) # your train set labels

    test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")
    test_set_x_orig = np.array(test_dataset["test_set_x"][:]) # your test set features
    test_set_y_orig = np.array(test_dataset["test_set_y"][:]) # your test set labels

    classes = np.array(test_dataset["list_classes"][:]) # the list of classes
    
    train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
    test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))
    
    return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


def show_cat(index, classes, train_set_y, train_set_x_orig):
    # Example of a 'cat' image
    plt.imshow(train_set_x_orig[index])
    print ("y = " + str(train_set_y[:, index]) + ", it's a '" +  classes[np.squeeze(train_set_y[:, index])].decode("utf-8") +  "' picture.")
    plt.savefig('img/preview.png', bbox_inches='tight')


def sigmoid(Z):
    """
    Implements the sigmoid activation in numpy
    
    Arguments:
    Z -- numpy array of any shape
    
    Returns:
    A -- output of sigmoid(z), same shape as Z
    cache -- returns Z as well, useful during backpropagation
    """
    
    A = 1/(1+np.exp(-Z))
    cache = Z
    
    return A, cache

def relu(Z):
    """
    Implement the RELU function.

    Arguments:
    Z -- Output of the linear layer, of any shape

    Returns:
    A -- Post-activation parameter, of the same shape as Z
    cache -- a python dictionary containing "A" ; stored for computing the backward pass efficiently
    """
    
    A = np.maximum(0,Z)
    
    assert(A.shape == Z.shape)
    
    cache = Z 
    return A, cache


def relu_backward(dA, cache):
    """
    Implement the backward propagation for a single RELU unit.

    Arguments:
    dA -- post-activation gradient, of any shape
    cache -- 'Z' where we store for computing backward propagation efficiently

    Returns:
    dZ -- Gradient of the cost with respect to Z
    """
    
    Z = cache
    dZ = np.array(dA, copy=True) # just converting dz to a correct object.
    
    # When z <= 0, you should set dz to 0 as well. 
    dZ[Z <= 0] = 0
    
    assert (dZ.shape == Z.shape)
    
    return dZ

def sigmoid_backward(dA, cache):
    """
    Implement the backward propagation for a single SIGMOID unit.

    Arguments:
    dA -- post-activation gradient, of any shape
    cache -- 'Z' where we store for computing backward propagation efficiently

    Returns:
    dZ -- Gradient of the cost with respect to Z
    """
    
    Z = cache
    
    s = 1/(1+np.exp(-Z))
    dZ = dA * s * (1-s)
    
    assert (dZ.shape == Z.shape)
    
    return dZ

def plot_costs(costs, learning_rate):
    """
    This function plots the cost values over iterations.

    Parameters:
    costs (list or array-like): The cost values at each iteration.
    learning_rate (float, optional): The learning rate used in the optimization algorithm. Default is 0.0075.

    Returns:
    None
    """
    
    # Set the style of the plot
    sns.set_style("whitegrid")
    
    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(np.squeeze(costs), color='purple')
    
    # Add a title and labels
    plt.title("Cost Over Time with Learning Rate = " + str(learning_rate), fontsize=16)
    plt.xlabel('Iterations (per hundreds)', fontsize=14)
    plt.ylabel('Cost', fontsize=14)
    
    # Add a grid
    plt.grid(True, linestyle='--', alpha=0.6)
    
    # Show the plot
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
        plt.imshow(X[:,index].reshape(64,64,3), interpolation='nearest')
        plt.axis('off')
        plt.title("Prediction: " + classes[int(p[0,index])].decode("utf-8") + " \n Class: " + classes[y[0,index]].decode("utf-8"))
    plt.show()
