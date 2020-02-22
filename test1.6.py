import cv2 as cv
import numpy as np
# 像素运算


def add_demo(m1,m2):
    demo = cv.add(m1,m2)
    cv.imshow("add",demo)


def substract_demo(m1,m2):
    demo = cv.subtract(m1,m2)
    cv.imshow("substract",demo)


def divide_demo(m1,m2):
    demo = cv.divide(m1,m2)
    cv.imshow("divide",demo)


def multiply_demo(m1,m2):
    demo = cv.multiply(m1,m2)
    cv.imshow("multiply",demo)


def others(m1):
    m = cv.mean(m1)
    a,b = cv.meanStdDev(m1)
    print("三通道均值为:",m)
    print("均值:%s,方差:%s" % (a, b))

    cv.bit


pic1 = cv.imread("mywife.PNG")  # pic是一个矩阵(不仅仅是矩阵)
pic2 = cv.imread("wife.PNG")
# print(pic.shape)
cv.namedWindow("wifevswife",cv.WINDOW_AUTOSIZE)
cv.imshow("wifevswife", pic1)
add_demo(pic1,pic2)
substract_demo(pic1,pic2)
divide_demo(pic1,pic2)
multiply_demo(pic1,pic2)
# others(pic1)
cv.waitKey(0)
cv.destroyAllWindows()
