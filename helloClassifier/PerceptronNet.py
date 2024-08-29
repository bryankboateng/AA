import numpy as np
from Perceptron import Perceptron
from numpy import ndarray

class PerceptronNet(object):
    def __init__(self, classes:int, inputs:int):
        self.classes = classes
        self.inputs = inputs
        self.perceptronNet : list[Perceptron] = []
        for _ in range(self.classes):
            self.perceptronNet.append(Perceptron(self.inputs))
        
    def __str__(self) -> str:
        return str(self.perceptronNet)
            
    def number_classes(self) -> int:
        return self.classes
    def number_inputs(self) -> int:
        return self.inputs
    # returns idx of class/perceptron with highest FP value
    def netPredict(self,x:ndarray) -> int:
        return np.argmax([perceptron.FP(x) for perceptron in self.perceptronNet])
    # positively trains perceptron with idx matching label negatively trains all others
    def netBP(self,x:ndarray,label:int):
        idx = 0
        for perceptron in self.perceptronNet:
            if idx == label:
                perceptron.BP(x,1)
            else:
                perceptron.BP(x,-1)
            idx+=1
            
