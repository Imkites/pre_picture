import cv2
'''
    #旋转效果
    image : 输入处理图像  
    angle : 旋转角度   
'''
def rotate_Img(image, angle):
    h, w= image.shape[ :2]
    matRotate = cv2.getRotationMatrix2D((w*0.5,h*0.5), angle, 1)
    dst = cv2.warpAffine(image, matRotate, (w,h))
    return  dst
