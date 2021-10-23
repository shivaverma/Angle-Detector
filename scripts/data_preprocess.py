import os
import json
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split


def preprocess(im):
    
    im = im/255
    im -= 0.5
    return im.astype('float16')


def get_data(start=0, end=None, batch_size=None, channel=3, im_size=128, data_path='out_data/'):
    
    '''
        This function create a batch of training data
    '''
    
    label = json.load(open("{}/label.json".format(data_path)))   
    if not end:
        end = len(label)
    batch_size = end - start
    label = label[start:end]
    label = np.array(label).astype('float16').reshape((batch_size, 1))/30
    image_batch = np.zeros((batch_size, im_size, im_size, channel)).astype('float16')  
    
    for i in range(start, end):
        im = Image.open("{}/images/{}.jpg".format(data_path, i))
        im = np.array(im)
        image_batch[i-start] = preprocess(im).reshape((im_size, im_size, channel))
            
    return (image_batch, label)