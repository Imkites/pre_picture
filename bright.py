import cv2
import numpy as np
'''
    #亮度变化
    image : 输入处理图像
    c : 图片image的权值
    b : 偏差
'''
def bright_Img(image, c, b):
    rows, cols, channels = image.shape
    blank = np.zeros([rows, cols, channels], image.dtype)
    rst = cv2.addWeighted(image, c, blank, 1 - c, b)
    return rst