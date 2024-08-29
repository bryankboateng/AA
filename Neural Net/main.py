import random
import matplotlib.pyplot as plt
import numpy as np
from Funcs import RELU, softmax, rescale
from NN import Linear
from Loss import cross_entropy_gradient 
from Module import Module
from os.path import join
from mnistLoader import MnistDataloader
from pathlib import Path


CLASSES: int = 10
INPUTS: int = 28 * 28

class NeuralNet(Module):
    def __init__(self):
        super().__init__()
        self.linear1 = Linear(16,INPUTS)
        self.relu1 = RELU()
        self.linear2 = Linear(16,16)
        self.relu2 = RELU()
        self.linear3 = Linear(CLASSES,16)
    
    def forward(self,x):
        x = self.linear1(x)
        x = self.relu1(x)
        x = self.linear2(x)
        x = self.relu2(x)
        x = self.linear3(x)
        x = softmax(x)
        return x
    
    def backward(self, grad_output):
        grad_output = self.linear3.backward(grad_output)
        grad_output = self.relu2.backward(grad_output)
        grad_output = self.linear2.backward(grad_output)
        grad_output = self.relu1.backward(grad_output)
        grad_output = self.linear1.backward(grad_output) 






# Helper function to show a list of images with their relating titles
def show_images(images, title_texts):
    cols = 5
    rows = int(len(images)/cols) + 1
    plt.figure(figsize=(30,20))
    index = 1    
    for x in zip(images, title_texts):        
        image = x[0]        
        title_text = x[1]
        ax = plt.subplot(rows, cols, index)        
        ax.imshow(image, cmap=plt.cm.gray)
        if (title_text != ''):
            ax.set_title(title_text, fontsize=8)
        
        # Remove x and y-axis ticks
        ax.set_xticks([])
        ax.set_yticks([])
        
        index += 1
    
    # Add plt.show() at the end to actually display the plot
    plt.show()
if __name__ == '__main__':
    input_path = Path.cwd().parent / 'data' / 'archive'
    training_images_filepath = join(input_path, 'train-images-idx3-ubyte/train-images-idx3-ubyte')
    training_labels_filepath = join(input_path, 'train-labels-idx1-ubyte/train-labels-idx1-ubyte')
    test_images_filepath = join(input_path, 't10k-images-idx3-ubyte/t10k-images-idx3-ubyte')
    test_labels_filepath = join(input_path, 't10k-labels-idx1-ubyte/t10k-labels-idx1-ubyte')

    #
    # Load MINST dataset
    #
    mnist_dataloader = MnistDataloader(training_images_filepath, training_labels_filepath, test_images_filepath, test_labels_filepath)
    (x_train, y_train), (x_test, y_test) = mnist_dataloader.load_data()




    #
    # Show some random training and test images 
    #
    images_2_show = []
    titles_2_show = []
    for i in range(0, 10):
        r = random.randint(1, 60000)
        images_2_show.append(x_train[r])
        titles_2_show.append('training image [' + str(r) + '] = ' + str(y_train[r]))    

    for i in range(0, 5):
        r = random.randint(1, 10000)
        images_2_show.append(x_test[r])        
        titles_2_show.append('test image [' + str(r) + '] = ' + str(y_test[r]))    

    show_images(images_2_show, titles_2_show)



    # Init feed forward neural network
    nn = NeuralNet()

    for (train_image,train_label) in zip(x_train,y_train): # zip image array and respective label
        output=nn(rescale(train_image.flatten()))
        one_hot = np.zeros(10)
        one_hot[train_label]=1
        grad_output = cross_entropy_gradient(output,one_hot)
        nn.backward(grad_output) 

    total_tests = 0
    success = 0    
    for (test_image,test_label) in zip(x_test,y_test): # zip image array and respective label
        output=nn(rescale(test_image.flatten()))
        prediction = np.argmax(output)
        if prediction == test_label:
            success += 1
        total_tests +=1
        
    print(f"Success rate of NeuralNet Model:{success/total_tests}")