from os.path import join
from mnistLoader import MnistDataloader
from PerceptronNet import PerceptronNet
from pathlib import Path

import random
import matplotlib.pyplot as plt
import numpy as np



CLASSES: int = 10
INPUTS: int = 28 * 28



# Helper function to show a list of images with their relating titles
#
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

# Helper function to rescale inputs to [0,1] range
def rescale(var:np.ndarray):
    return (var - np.min(var)) / (np.max(var) - np.min(var))

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

    # print(type(x_train[0])) # ndarray
    # print(x_train[0].shape) # (28,28)
    # print(type(y_train[0]))  #  int


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



    mp = PerceptronNet(CLASSES,INPUTS)

    for (train_image,train_label) in zip(x_train,y_train): # zip image array and respective label
        #train_image = rescale(train_image) 
        mp.netBP(train_image.flatten(),train_label)
        

    total_tests = 0
    success = 0    
    for (test_image,test_label) in zip(x_test,y_test): # zip image array and respective label
        #test_image = rescale(test_image)
        prediction = mp.netPredict(test_image.flatten())
        if prediction == test_label:
            success += 1
        total_tests +=1
        
    print(f"Success rate of PerceptronNet Model:{success/total_tests}")
    # Success rate drops from .8475 to .8162 with rescaling