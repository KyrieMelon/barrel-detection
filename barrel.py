
import cv2
from color_seg import ColorSegmentation
import numpy as np
from find_box import findBox, drawCorner
import matplotlib.pyplot as plt




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
filename = r"./trainset/43.png"
img = cv2.imread('%s' % filename)
CS = ColorSegmentation(DATA_SET)
pic = CS.seg(img)

boxes = findBox(pic)

for barrel in boxes:
    cv2.rectangle(pic, (barrel[0], barrel[1]), (barrel[2], barrel[3]),(0, 255, 0), 2)
    # cv2.drawContours(pic, [barrel['box']], -1, (255, 255, 255), 2)
    # draw_corner(pic, barrel['box'])
    print(barrel)

cv2.imshow('new',pic)
cv2.waitKey()
cv2.destroyAllWindows()
