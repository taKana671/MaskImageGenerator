import numpy as np

import cv2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class RadialGradient:
    """A class to create radial gradient mask image.
        Arges:
            height (int): The height of an image.
            width (int): The width of an image.
            center_h (int): y-axis center; must be positive; heght // 2, if not specified.
            center_w (int): x-axis center; must be positive; width // 2, if not specified.
            gradient_size (float): The larger the gradient_size, the smaller the 
            circle of the gradient become.
            inner_color (tuple|list) : A tuple or list of three elements, with values ranging from 0 to 255.
            outer_color (tuple|list) : A tuple or list of three elements, with values ranging from 0 to 255.
    """

    def __init__(self, height=256, width=256, center_h=None, center_w=None, gradient_size=2,
                 inner_color=BLACK, outer_color=WHITE, inner_alpha=255, outer_alpha=0):
        self.height = height
        self.width = width
        self.gradient_size = gradient_size
        self.inner_color = [v / 255 for v in inner_color]
        self.outer_color = [v / 255 for v in outer_color]
        self.inner_alpha = inner_alpha / 255
        self.outer_alpha = outer_alpha / 255

        self.center = self.define_center(center_h, center_w)
        self.max_length = max(self.height, self.width)

    def define_center(self, center_h, center_w):
        center = np.zeros(2)

        if center_w is None or not 0 <= center_w <= self.width:
            center[0] = self.width // 2
        else:
            center[0] = center_w

        if center_h is None or not 0 <= center_h <= self.height:
            center[1] = self.height // 2
        else:
            center[1] = center_h

        return center

    def get_gradient(self, x, y):
        dist_to_center = ((x - self.center[0]) ** 2 + (y - self.center[1]) ** 2) ** 0.5
        dist = dist_to_center / (2 ** 0.5 * self.max_length / self.gradient_size)

        if dist >= 1:
            r, g, b = self.outer_color
        else:
            r = self.outer_color[0] * dist + self.inner_color[0] * (1 - dist)
            g = self.outer_color[1] * dist + self.inner_color[1] * (1 - dist)
            b = self.outer_color[2] * dist + self.inner_color[2] * (1 - dist)

        return (r, g, b)

    def get_transparent_gradient(self, x, y):
        dist_to_center = ((x - self.center[0]) ** 2 + (y - self.center[1]) ** 2) ** 0.5
        dist = dist_to_center / (2 ** 0.5 * self.max_length / self.gradient_size)

        if dist >= 1:
            alpha = self.outer_alpha
            r, g, b = self.outer_color
        else:
            alpha = self.inner_alpha * (1 - dist)
            r = self.outer_color[0] * dist + self.inner_color[0] * (1 - dist)
            g = self.outer_color[1] * dist + self.inner_color[1] * (1 - dist)
            b = self.outer_color[2] * dist + self.inner_color[2] * (1 - dist)
        
        return (r, g, b, alpha)

    def get_grad_array(self):
        arr = np.array(
            [self.get_gradient(x, y)
                for y in range(self.height)
                for x in range(self.width)]
        )

        arr = arr.reshape(self.height, self.width, 3)
        return arr

    def get_transparent_grad_array(self):
        arr = np.array(
            [self.get_transparent_gradient(x, y)
                for y in range(self.height)
                for x in range(self.width)]
        )

        arr = arr.reshape(self.height, self.width, 4)
        return arr

    def output_8bit_image(self, file_path, arr):
        arr = np.clip(arr * 255, a_min=0, a_max=255).astype(np.uint8)
        cv2.imwrite(file_path, arr)




if __name__ == '__main__':
    grad = RadialGradient(height=129, width=129)
    # grad.get_radial_gradient_img()
    arr = grad.get_transparent_grad_array()
    grad.output_8bit_image('trans_grad_img_0.png', arr)






        

