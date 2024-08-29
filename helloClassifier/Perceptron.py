import numpy as np
from numpy import ndarray


class Perceptron(object):
    def __init__ (self,len:int):
        self.len = len
        self.perceptron = np.array([0]*self.len)
    
    # override for string representation of Perceptron
    def __str__(self) -> str:
        return str(self.perceptron)
    
    # returns length of Perceptron    
    def len(self):
        return self.len
    
    # returns inner product of perceptron and input vector # forward prop   
    def FP(self, x:ndarray): # type(x) = np.array
        return np.dot(x,self.perceptron)
    
    # predicts label of input (1 or -1)
    # returns 1 if inner product > 0, returns -1 if negative or zero 
    def predict(self,x:ndarray) -> int:
        if self.FP(x) > 0:
            return 1
        else :
            return -1
        
     # modifies perceptron based on labeled input 1 or -1  # back prop 
    def BP(self,x:ndarray,label:int):  # label = 1 or label = -1
        modification = 0
        if self.predict(x) > label:
            modification = -1
        if self.predict(x) < label:
            modification = 1
        self.perceptron = self.perceptron + modification * x
        
if __name__ == 'main':
    myPerceptron = Perceptron(2)
    print(myPerceptron)
    myX = np.array([0,1])
    print(f"Prediction6: {myPerceptron.predict(myX)}")
    myPerceptron.BP(myX,1)
    print(myPerceptron)
