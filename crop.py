import random
import numpy as np
'''
    # 随机裁剪
    image : 输入处理图像
    min_ratio : 最小裁剪比例
    max_ratio : 最大裁剪比例
'''
def random_crop(image, min_ratio, max_ratio):
    h, w = image.shape[:2]
    ratio = random.random()
    scale = min_ratio + ratio * (max_ratio - min_ratio)
    new_h = int(h * scale)
    new_w = int(w * scale)
    y = np.random.randint(0, h - new_h)
    x = np.random.randint(0, w - new_w)
    image = image[y:y + new_h, x:x + new_w, :]
    return image
