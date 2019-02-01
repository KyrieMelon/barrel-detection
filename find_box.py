import numpy as np
import cv2
import math

def findBox(pic):
    bwpic = np.array(pic[:, :, 2], dtype=np.uint8)
    #median filter
    bwpic = cv2.medianBlur(bwpic, 5)
    bwpic, contours, hierarchy = cv2.findContours(bwpic, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    areas = [cv2.contourArea(cnt) for cnt in contours]

    result = []
    for cnt in contours:
        # rect = cv2.minAreaRect(cnt)
        # box = cv2.boxPoints(rect)
        # box = np.int0(box)
        x, y, w, h = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)

        if np.max(areas) <= 4 * area and (h / w >= 1) and (h / w <= 3):
            result.append([x, y, x + w, y + h])

    return result


def drawCorner(pic,boxs):
    for box in boxs:
        cv2.circle(pic,tuple(box), 5, (0, 0, 0))
