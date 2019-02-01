import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np 
from roipoly import roipoly
import random
import os

folder_to_save_img = './not_blue'

def get_img_from_mask(old_img,mask):
    ny,nx = np.shape(mask)
    max_x = 0
    min_x = nx
    max_y = 0
    min_y = ny
    for x in range(0,nx):
        for y in range(0,ny):
            if mask[y][x] == True:
                max_x = max(x, max_x)
                max_y = max(y, max_y)
                min_x = min(x, min_x)
                min_y = min(y, min_y)
            else:
                # let other part be white
                old_img[y][x][0] = 0
                old_img[y][x][1] = 0
                old_img[y][x][2] = 0

    new_img = old_img[min_y : max_y, min_x : max_x]
    return  new_img

def save_new_img(new_img):
    name = os.path.join(folder_to_save_img,str(random.random()) + '.png')
    print(name)
    plt.imsave(name, new_img,format = 'png')

def label(filename):
    img = plt.imread(filename)
    plt.title('Label function')
    plt.imshow(img)
    plt.colorbar()
    roi = roipoly(roicolor = 'r')
    mask = roi.getMask(img[:,:,0])
    new_img = get_img_from_mask(img,mask)
    save_new_img(new_img)

if __name__ == "__main__":
    
    filedict = []
    for item in os.walk('./trainset'):
        filedict = item[2]
    random.shuffle(filedict)
    for item in filedict:
        filename = os.path.join('./trainset',item)
        label(filename)
