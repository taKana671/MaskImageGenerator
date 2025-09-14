import cv2
import numpy as np

from ..utils import output_image


class Lines:

    def __init__(self, bg_color, line_color, height=256, width=256, gaussian_kernel=31):
        self.height = 256
        self.width = 256
        self.gaussian_kernel = gaussian_kernel
        self.line_color = line_color
        self.bg_color = bg_color
        
        # self.img = np.zeros((height, width), dtype=np.uint8)
        # dim = (height, width, len(bg_color))
        # self.img = np.full(dim, bg_color, dtype=np.uint8)

    def create_lines(self, coordinates, thickness=5, arr=None):
        if arr is None:
            dim = (self.height, self.width, len(self.bg_color))
            img = np.full(dim, self.bg_color, dtype=np.uint8)

        for start_pt, end_pt in coordinates:
            cv2.line(self.img, start_pt, end_pt, self.line_color, thickness=thickness, lineType=cv2.LINE_AA)

    def blur(self):
        self.img = cv2.GaussianBlur(self.img, (self.gaussian_kernel, self.gaussian_kernel), 0)
        # return img_blur


class LineMask(Lines):

    def __init__(self, height=256, width=256, gaussian_kernel=31):
        super().__init__(
            bg_color=(0, 0, 0),
            line_color=(255, 255, 255),
            height=height,
            width=width,
            gaussian_kernel=gaussian_kernel
        )

    @staticmethod
    def output_image(coordinates, height=256, width=256, gaussian_kernel=31, line_thickness=5):
        generator = LineMask(height, width, gaussian_kernel)
        generator.create_lines(coordinates, line_thickness)

        if generator.gaussian_kernel is not None:
            generator.blur()

        output_image(generator.img, 'line_mask')


class TransparentLineMask(Lines):

    def __init__(self, height=256, width=256, gaussian_kernel=31):
        super().__init__(
            bg_color=(0, 0, 0, 255),
            line_color=(255, 255, 255, 255),
            height=height,
            width=width,
            gaussian_kernel=gaussian_kernel
        )

    def make_transparent(self):
        self.img[:, :, 3] -= self.img[:, :, 0]

    @staticmethod
    def output_image(coordinates, height=256, width=256, gaussian_kernel=31, line_thickness=5):
        generator = TransparentLineMask(height, width, gaussian_kernel)
        generator.create_lines(coordinates, line_thickness)

        if generator.gaussian_kernel is not None:
            generator.blur()

        generator.make_transparent()
        output_image(generator.img, 'line_mask')


def create_mask(points, thickness=5, size=256):
    img = np.zeros((size, size), dtype=np.uint8)
    color = (255, 255, 255)

    for start_pt, end_pt in points:
        cv2.line(img, start_pt, end_pt, 255, thickness=thickness, lineType=cv2.LINE_AA)
    
    cv2.imwrite('test.png', img)



if __name__ == '__main__':
    points = [[(0, 0), (256, 256)], [(0, 128), (256, 128)], [(128, 0), (128, 256)], [(0, 256), (256, 0)]]
    create_mask(points)



