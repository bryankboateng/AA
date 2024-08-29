import numpy as np



def bin_entropy_loss(output, target):
    loss = -target * np.log(output) - (1 - target) * np.log(1 - output)
    return np.sum(loss)

def bin_entropy_gradient(output, target):
    return (output - target) / (output * (1 - output))

def cross_entropy_loss(output, target):
    # expect the target to be a one-hot encoding
    # expect output to be probs
    loss = -target * np.log(output)
    return loss

def cross_entropy_gradient(output, target):
    # expect the target to be a one-hot encoding
    # expect output to be probs
    return (output - target)
