import numpy as np

import cv2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class RadialGradient:

    def __init__(self, height=256, width=256, center_h=None, center_w=None,
                 inner_color=BLACK, outer_color=WHITE):
        self.height = height
        self.width = width
        self.inner_color = [v / 255 for v in inner_color]
        self.outer_color = [v / 255 for v in outer_color]

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
        dist = dist_to_center / (2 ** 0.5 * self.max_length / 2)

        if dist >= 1:
            r, g, b = self.outer_color
        else:
            r = self.outer_color[0] * dist + self.inner_color[0] * (1 - dist)
            g = self.outer_color[1] * dist + self.inner_color[1] * (1 - dist)
            b = self.outer_color[2] * dist + self.inner_color[2] * (1 - dist)

        return (r, g, b)

    def get_gradient_array(self):
        arr = np.array(
            [self.get_gradient(x, y)
                for y in range(self.height)
                for x in range(self.width)]
        )

        arr = arr.reshape(self.height, self.width, 3)
        return arr

    def output_8bit_image(self, file_path):
        arr = self.get_gradient_array()
        arr = np.clip(arr * 255, a_min=0, a_max=255).astype(np.uint8)
        cv2.imwrite(file_path, arr)




if __name__ == '__main__':
    grad = RadialGradient(inner_color = (255, 0, 0), outer_color=(255, 255, 255))
    # grad.get_radial_gradient_img()
    grad.output_8bit_image('grad_img_1.png')






        

