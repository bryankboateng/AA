#
import numpy as np # linear algebra

import struct 
# struct is a module that facilatates conversions between python values and C structs(in the form of Python byte objects)
# struct packing and unpacking is accomplished with format string (representing dtypes and endianness) and values
# endianness allows us to order bytes: big endianess stores biggerst bit in smallest address val and vice-versa
# This is similar to regular language for digits read from left to right

from array import array



#
# MNIST Data Loader Class
#
class MnistDataloader(object):
    def __init__(self, training_images_filepath,training_labels_filepath,
                 test_images_filepath, test_labels_filepath):
        self.training_images_filepath = training_images_filepath
        self.training_labels_filepath = training_labels_filepath
        self.test_images_filepath = test_images_filepath
        self.test_labels_filepath = test_labels_filepath
    
    # recieves path for encoded img and label then returns representative arrays
    def read_images_labels(self, images_filepath, labels_filepath):        
        labels = []
        with open(labels_filepath, 'rb') as file:
            magic, size = struct.unpack(">II", file.read(8)) # I - 4 bytes(usigned integer) # > - big endianness
            if magic != 2049: # magic number is part of the mnist fmt to ensure distinction between files
                raise ValueError('Magic number mismatch, expected 2049, got {}'.format(magic))
            labels = array("B", file.read()) # "B" implies that array dtypes is an unsigned char  - 1 byte       
        
        with open(images_filepath, 'rb') as file:
            magic, size, rows, cols = struct.unpack(">IIII", file.read(16))
            if magic != 2051:
                raise ValueError('Magic number mismatch, expected 2051, got {}'.format(magic))
            image_data = array("B", file.read())        
        images = []
        for i in range(size):
            images.append([0] * rows * cols) # intialize null image arrays to be filled
        for i in range(size):
            img = np.array(image_data[i * rows * cols:(i + 1) * rows * cols])
            img = img.reshape(28, 28)
            images[i][:] = img    
            # revisit line above and below for more effecient way of handling ndarray list conundrum 
            # 28 ndarrays of elements instead of a 28x28 ndarray
        images = np.array(images)            
        
        return images, labels
    # returns img and label for training and testing data respectively
    def load_data(self):
        x_train, y_train = self.read_images_labels(self.training_images_filepath, self.training_labels_filepath)
        x_test, y_test = self.read_images_labels(self.test_images_filepath, self.test_labels_filepath)
        return (x_train, y_train),(x_test, y_test)
    
    
    
# TRAINING SET IMAGE FILE (train-images-idx3-ubyte):
# [offset] [type]          [value]          [description] 
# 0000     32 bit integer  0x00000803(2051) magic number
# 0004     32 bit integer  60000            number of images 
# 0008     32 bit integer  28               number of rows 
# 0012     32 bit integer  28               number of columns