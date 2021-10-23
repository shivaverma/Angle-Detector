import os
import cv2
import json
import imutils
import numpy as np
import pandas as pd
from PIL import Image
from numpy import random
from matplotlib import pyplot as plt


def center_crop(img, dim):
    
    width, height = img.shape[1], img.shape[0]
    crop_width = dim[0] if dim[0]<img.shape[1] else img.shape[1]
    crop_height = dim[1] if dim[1]<img.shape[0] else img.shape[0] 
    mid_x, mid_y = int(width/2), int(height/2)
    cw2, ch2 = int(crop_width/2), int(crop_height/2) 
    crop_img = img[mid_y-ch2:mid_y+ch2, mid_x-cw2:mid_x+cw2]
    return crop_img


def get_random_angle():
    x = (random.rand()-0.5)*60
    return x


def rotate(image, angle):
    rotated = imutils.rotate_bound(image, angle)
    return rotated


def resize(image, shape, interpolation = cv2.INTER_AREA):
    resized = cv2.resize(image, (shape,shape))
    return resized


def process_imgs(inp_dir, out_dir):

    print("processoing folder: {}\n".format(inp_dir))
    os.system("mkdir -p {}".format(out_dir))
    ind = 0
    label = []
    final_shape = 128
    for folder in os.listdir(inp_dir):
        for img in os.listdir("{}/{}".format(inp_dir, folder)):
            try:
                image = cv2.imread("{}/{}/{}".format(inp_dir, folder, img))
                angle = get_random_angle()
                rotated = rotate(image, angle)
                rot_size = rotated.shape[0]
                deg_angle = abs((np.pi/180)*angle)
                crop_size = int(rot_size/(1+2*(np.sin(deg_angle))*(np.cos(deg_angle))))
                crop2 = center_crop(rotated, (crop_size, crop_size))
                resized = resize(crop2, final_shape)
                label.append(angle)
                cv2.imwrite("{}/{}.jpg".format(out_dir, ind), resized)
                ind = ind+1
                if ind%1000==0:
                    print("{} images done".format(ind))
            except:
                pass

    label = [round(i, 2) for i in label]
    json.dump(label, open("{}.json".format(out_dir), 'w'))
    
    
inp_dir = '/Users/shiva/Desktop/rotation/data'
out_dir = '/Users/shiva/Desktop/rotation/out_data'

process_imgs(inp_dir, out_dir)