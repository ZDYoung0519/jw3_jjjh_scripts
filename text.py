import os
import cv2
import time
import numpy as np
from matplotlib import pyplot as plt

def get_target_location(img_target, img_template):
    H, W = img_template.shape[:2]
    res = 1-cv2.matchTemplate(img_target, img_template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    center_loc = round(max_loc[0] + 0.5*W), round(max_loc[1] + 0.5*H)
    '''
    img = cv2.rectangle(img_target, max_loc, (max_loc[0] + W, max_loc[1] + H), (0, 0, 255), 3)
    img = cv2.circle(img, center_loc, 5, (0, 0, 255), -1)
    cv2.namedWindow('Image', 0)
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''
    return max_val, center_loc


def hold_on(self, location, last_time):
    os.system('adb shell input swipe ' +
              str(location[0]) + ' ' + str(location[1]) + ' ' + str(last_time))


def find_item_contours(img):
    img_gray = cv2.imread('../../用户/文档/Projects/ADB_jw3/doc/temp.png', cv2.IMREAD_GRAYSCALE)
    cannyPic = cv2.Canny(img_gray, 10, 200)
    contours, hierarchy = cv2.findContours(cannyPic, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    find_contours = []
    for i in range(len(contours)):
        if 20000 <= cv2.contourArea(contours[i]) <= 29000:
            # print(cv2.contourArea(contours[i]))
            loc1 = np.min(contours[i][:, :, 0]), np.min(contours[i][:, :, 1])
            loc2 = np.max(contours[i][:, :, 0]), np.max(contours[i][:, :, 1])
            find_contours.append([loc1, loc2])
    return find_contours

def match_templat(find_contours, tm_contours):
    return 0
t1 = time.time()
img = cv2.imread('../../用户/文档/Projects/ADB_jw3/doc/temp.png')
img_gray = cv2.imread('../../用户/文档/Projects/ADB_jw3/doc/temp.png', cv2.IMREAD_GRAYSCALE)
cv2.namedWindow('Image', 0)
cv2.imshow('Image', img_gray)
cannyPic = cv2.Canny(img_gray, 10, 200)
#cv2.namedWindow('cannyPic', 0)
#cv2.imshow('cannyPic', cannyPic)
contours, hierarchy = cv2.findContours(cannyPic, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
find_contours = []
for i in range(len(contours)):
    if 20000 <= cv2.contourArea(contours[i]) <= 29000:
        # print(cv2.contourArea(contours[i]))
        loc1 = np.min(contours[i][:, :, 0]), np.min(contours[i][:, :, 1])
        loc2 = np.max(contours[i][:, :, 0]), np.max(contours[i][:, :, 1])
        find_contours.append([loc1, loc2])
print(find_contours)
for i in range(len(find_contours)):

# cannyFind = cv2.drawContours(img, find_contours, -1, (0, 0, 255), 3, lineType=cv2.LINE_AA)
cannyFind = cv2.rectangle(img, find_contours[0][0], find_contours[0][1], (0, 0, 255), 5)
cv2.namedWindow('cannyFind', 0)
cv2.imshow('cannyFind', cannyFind)

t2 = time.time()
print(t2-t1)
cv2.waitKey(0)
cv2.destroyAllWindows()

