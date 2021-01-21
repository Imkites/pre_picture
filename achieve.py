import cv2
import matplotlib.pyplot as plt
import crop
import rotate
import bright

if __name__ == "__main__":

    img = cv2.imread("pig.jpg")
    img_rgb = img[:,:,[2,1,0]]
    cv2.imshow('img',img)


    new_image1 = crop.random_crop(img_rgb, 0.5, 1.0)
    plt.imshow(new_image1)
    plt.show()

    new_image2 = rotate.rotate_Img(img_rgb, 180)
    plt.imshow(new_image2)
    plt.show()

    # 第二个参数调节亮度，越大越亮，越小越暗
    new_image3 = bright.bright_Img(img_rgb, 1.5, 3)
    plt.imshow(new_image3)
    plt.show()