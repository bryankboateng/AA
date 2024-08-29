from typing import Any


class Module:
    def __init__(self) -> None:
        self._modules = []
        self._parameters = []
        
    def add_module(self, module):
        self._modules.append(module)
        
    def add_parameter(self, param):
        self._parameters.append(param)
        
    def clear_parameters(self):
        self._parameters.clear()
        
    def forward(self, *input):
        raise NotImplementedError
    
    def backward(self, grad_input):
        raise NotImplementedError
    
    def __call__(self, *input) -> Any:
        return self.forward(*input)
    