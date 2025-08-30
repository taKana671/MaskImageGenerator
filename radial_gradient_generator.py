import numpy as np

from utils import output_image


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
            inner_color (tuple|list): A tuple or list of three elements, with values ranging from 0 to 255.
            outer_color (tuple|list): A tuple or list of three elements, with values ranging from 0 to 255.
    """

    def __init__(self, height=256, width=256, center_h=None, center_w=None,
                 gradient_size=2, inner_color=BLACK, outer_color=WHITE):
        self.height = height
        self.width = width
        self.gradient_size = gradient_size
        # Change color range.
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

    def get_distance(self, x, y):
        norm = ((x - self.center[0]) ** 2 + (y - self.center[1]) ** 2) ** 0.5
        dist_to_center = norm / (2 ** 0.5 * self.max_length / self.gradient_size)
        return dist_to_center

    def get_gradient(self, x, y):
        dist = self.get_distance(x, y)

        if dist >= 1:
            return self.outer_color

        rgb = [self.outer_color[i] * dist + self.inner_color[i] * (1 - dist) for i in range(3)]
        return rgb

    def get_gradient_array(self):
        arr = np.array(
            [self.get_gradient(x, y)
                for y in range(self.height)
                for x in range(self.width)]
        )
        arr = arr.reshape(self.height, self.width, 3)
        return arr

    @staticmethod
    def output_image(height=256, width=256, center_h=None, center_w=None, gradient_size=2,
                     inner_color=BLACK, outer_color=WHITE, output_dir=None):
        generator = RadialGradient(
            height=height,
            width=width,
            center_h=center_h,
            center_w=center_w,
            gradient_size=gradient_size,
            inner_color=inner_color,
            outer_color=outer_color
        )

        arr = generator.get_gradient_array()
        output_image(arr, 'radial_gradient', output_dir)


class TransparentRadialGradient(RadialGradient):
    """A class to create transparent radial gradient mask image.
        Arges:
            height (int): The height of an image.
            width (int): The width of an image.
            center_h (int): y-axis center; must be positive; heght // 2, if not specified.
            center_w (int): x-axis center; must be positive; width // 2, if not specified.
            gradient_size (float): The larger the gradient_size, the smaller the
            circle of the gradient become.
            inner_color (tuple|list): A tuple or list of three elements, with values ranging from 0 to 255.
            outer_color (tuple|list): A tuple or list of three elements, with values ranging from 0 to 255.
            inner_alpha (int): Alpha value at the start of the transparent gradient, with values ranging from 0 to 255.
            outer_alpha (int): Alpha value at the end of the transparent gradient, with values ranging from 0 to 255.
    """

    def __init__(self, height=256, width=256, center_h=None, center_w=None, gradient_size=2,
                 inner_color=BLACK, outer_color=WHITE, inner_alpha=255, outer_alpha=0):
        super().__init__(
            height=height,
            width=width,
            center_h=center_h,
            center_w=center_w,
            gradient_size=gradient_size,
            inner_color=inner_color,
            outer_color=outer_color
        )
        # Change color range.
        self.inner_alpha = inner_alpha / 255
        self.outer_alpha = outer_alpha / 255

    def get_gradient(self, x, y):
        dist = self.get_distance(x, y)

        if dist >= 1:
            return (*self.outer_color, self.outer_alpha)

        rgb = [self.outer_color[i] * dist + self.inner_color[i] * (1 - dist) for i in range(3)]
        alpha = self.inner_alpha * (1 - dist)
        return (*rgb, alpha)

    def get_gradient_array(self):
        arr = np.array(
            [self.get_gradient(x, y)
                for y in range(self.height)
                for x in range(self.width)]
        )
        arr = arr.reshape(self.height, self.width, 4)
        return arr

    @staticmethod
    def output_image(height=256, width=256, center_h=None, center_w=None, gradient_size=2,
                     inner_color=BLACK, outer_color=WHITE, inner_alpha=255, outer_alpha=0, output_dir=None):
        generator = TransparentRadialGradient(
            height=height,
            width=width,
            center_h=center_h,
            center_w=center_w,
            gradient_size=gradient_size,
            inner_color=inner_color,
            outer_color=outer_color,
            inner_alpha=inner_alpha,
            outer_alpha=outer_alpha
        )

        arr = generator.get_gradient_array()
        output_image(arr, 'transparent_radial_gradient', output_dir)


if __name__ == '__main__':
    RadialGradient.output_image()
