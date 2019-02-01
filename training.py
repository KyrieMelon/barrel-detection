
import cv2
import matplotlib.pyplot as plt
import os
import numpy as np

DATA_SET_NAME = 'not_blue'

training_set_folder = './%s'%DATA_SET_NAME # blue or not blue
HSV_DATA_SET = []

def get_all_filenames():
    filedict = []
    for item in os.walk(training_set_folder):
        filedict = item[2]
    
    filedict = [os.path.join(training_set_folder,x) for x in filedict]
    return filedict

def extract(img): 
    # convert img to HSV
    # return the  
    hsv = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    ny,nx,nz = np.shape(hsv)
    # print(np.shape(hsv))
    for x in range(0, nx):
        for y in range(0, ny):
            if not np.array_equal(hsv[y,x],np.array([0,0,0])):
                if not hsv[y,x].tolist() in HSV_DATA_SET:
                    HSV_DATA_SET.append(hsv[y,x].tolist())


if __name__ == '__main__':
    filedict = get_all_filenames()
    pool = []

    for item in filedict:
        img = cv2.imread(item)
        print(item)
        extract(img)

    f = open('./%s.txt'%DATA_SET_NAME,'w')
    
    for item in HSV_DATA_SET:
        f.write('%d %d %d \n'%(item[0],item[1],item[2]))

    f.close()




