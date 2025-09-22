import cv2
import numpy as np


class ShapeMask:
    """A class to draw a shape on an image.
        Arge:
            bg_color (tuple or list): The background color of an image; values ranging from 0 to 255.
            height (int): The height of an image; default is 256.
            width (int): The width of an image; default is 256.
            gaussian_kernel (int):
                The size of gaussian kernel; must be an odd number;
                if None is specified, no blurring; default is None.
    """

    def __init__(self, bg_color, height=256, width=256, gaussian_kernel=None):
        self.height = height
        self.width = width
        self.gaussian_kernel = gaussian_kernel
        self.bg_color = bg_color

    def create_bg_image(self):
        dim = (self.height, self.width, len(self.bg_color))
        img = np.full(dim, self.bg_color, dtype=np.uint8)
        return img

    def blur(self, img):
        return cv2.GaussianBlur(img, (self.gaussian_kernel, self.gaussian_kernel), 0)

    def change_rgb_to_bgr(self, img):
        img = img[:, :, ::-1]
        return img