

from gaussian import GaussianModel
from matplotlib import pyplot
import numpy as np
import cv2

class ColorSegmentation:
    def __init__(self,DATA_SET):

        self.DATA_SET = DATA_SET
        # Color Segmentation Class
        for catagory in range(len(self.DATA_SET)):
            x, y, z = [], [], []
            for item in open('./%s.txt'%(self.DATA_SET[catagory]['name']), 'r'):
                str_data = item.split(' ')
                x.append(int(str_data[0]))
                y.append(int(str_data[1]))
                z.append(int(str_data[2]))

            X = np.array([x, y, z]).T
            self.DATA_SET[catagory]['X'] = X
            self.DATA_SET[catagory]['GM'] = GaussianModel(X)

    def seg(self, img):

        hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
        ny, nx, nz = np.shape(hsv)

        pic = np.zeros((ny, nx, 3))

        for i in range(ny // 2):
            for j in range(nx // 2):

                rlt = [self.DATA_SET[GM]['GM'].gx(hsv[i * 2, j * 2, :]) for GM in range(len(self.DATA_SET))]
                if rlt[0] == min(rlt):
                    pic[i * 2 : i * 2 + 2, j * 2 : j * 2 + 2, 2] = 1

        return pic


if __name__ == '__main__':
    DATA_SET = [
        {
            'name': 'blue',
            'X': None,
            'GM': None,
            'mask': 2
        },
        {
            'name': 'not_barrel_blue',
            'X': None,
            'GM': None,
            'mask': 1

        },

        {
            'name': 'not_blue',
            'X': None,
            'GM': None,
            'mask': 0
        }
    ]
    filename = r"./trainset/28.png"
    img = cv2.imread('%s' % filename)
    CS = ColorSegmentation(DATA_SET)
    pic = CS.seg(img)
    # mask = pic[:, :, 2]
    # cv2.imshow('2', mask)
    # cv2.waitKey()
