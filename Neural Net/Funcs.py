from typing import Any
import numpy as np
from Module import Module

class RELU(Module):
    def forward(self, x):
        self.input = x
        output = np.maximum(0,x)
        return output
    
    def backward(self, grad_input):
        indicator = (self.input > 0).astype(int)
        grad_output = grad_input @ np.diag(indicator)
        return grad_output
    

def softmax(x):
    # Subtract the max value for numerical stability
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0, keepdims=True)

def rescale(var:np.ndarray):
    return (var - np.min(var)) / (np.max(var) - np.min(var))