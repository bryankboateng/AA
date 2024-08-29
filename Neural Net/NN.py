from typing import Any
import numpy as np
from Module import Module

class Linear(Module):
    def __init__(self, outputDim, inputDim,weights=np.empty((0,1)),withBias=True) -> None:
        super().__init__()
        #self.weights = np.random.normal(0,1,(outputDim,inputDim))
        # He intialization for stability
        if not weights.size:
            self.weights = np.random.normal(0, np.sqrt(2 / inputDim), (outputDim, inputDim))
        else:
            self.weights = weights
        self.bias = np.zeros(outputDim)
        self.add_parameter([self.weights, self.bias])
        self.withBias = withBias

    
    def forward(self, x):
        self.input = x
        return self.weights @ x + self.bias
    
    def backward(self, grad_input):
        # process
        grad_output = grad_input @ self.weights
        weight_update = np.outer(grad_input, self.input)
        # update
        if self.withBias:
            bias_update = grad_input
            self.bias -= .01 * bias_update
        self.weights -= .01 * weight_update
        self.clear_parameters()
        self.add_parameter([self.weights, self.bias])
        # return
        return grad_output
        
    

# if __name__ == '__main__':
#     # myNN = NN(2,5)
#     # input_v = np.random.normal(0,1,(2,1))
#     # print(myNN(input_v))
    
    
