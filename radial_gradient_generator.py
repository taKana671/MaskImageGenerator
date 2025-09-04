import numpy as np

from .utils import output_image


class RadialGradient:
    """A class to generate radial gradient.
        Arges:
            height (int): The height of an image.
            width (int): The width of an image.
            inner_color (tuple or list):
                The starting color of gradient; values ranging from 0 to 255;
                the number of elements must be the same as outer_color.
            outer_color (tuple or list):
                The end color of gradient; values ranging from 0 to 255;
                the number of elements must be the same as inner_color.
            gradient_size (float):
                The larger the gradient_size, the smaller the circle of the gradient become.
            center_h (int): y-axis center; must be positive; heght // 2, if not specified.
            center_w (int): x-axis center; must be positive; width // 2, if not specified.
    """

    def __init__(self, height, width, inner_color, outer_color,
                 gradient_size=2, center_h=None, center_w=None):
        self.height = height
        self.width = width
        self.gradient_size = gradient_size
        # Change color range.
        self.inner_color = [v / 255 for v in inner_color]
        self.outer_color = [v / 255 for v in outer_color]

        self.center = self.define_center(center_h, center_w)
        self.max_length = max(self.height, self.width)
        self.channels = len(self.inner_color)

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

        rgb = [self.outer_color[i] * dist + self.inner_color[i] * (1 - dist) for i in range(self.channels)]
        return rgb

    def get_gradient_array(self):
        arr = np.array(
            [self.get_gradient(x, y)
                for y in range(self.height)
                for x in range(self.width)]
        )
        arr = arr.reshape(self.height, self.width, self.channels)
        return arr

    def output(self, arr, img_type, output_dir=None):
        arr = np.clip(arr * 255, a_min=0, a_max=255).astype(np.uint8)
        output_image(arr, img_type, output_dir)

    @staticmethod
    def output_image(inner_color, outer_color, height=256, width=256,
                     gradient_size=2, center_h=None, center_w=None):
        generator = RadialGradient(
            inner_color=inner_color,
            outer_color=outer_color,
            height=height,
            width=width,
            gradient_size=gradient_size,
            center_h=center_h,
            center_w=center_w,
        )

        arr = generator.get_gradient_array()
        generator.output(arr, 'color_radial_gradient')


class RadialGradientMask(RadialGradient):
    """A class to generate black and white radial gradient.
        Arges:
            height (int): The height of an image.
            width (int): The width of an image.
            center_h (int): y-axis center; must be positive; heght // 2, if not specified.
            center_w (int): x-axis center; must be positive; width // 2, if not specified.
            gradient_size (float):
                The larger the gradient_size, the smaller the circle of the gradient become.
            inner_to_outer (bool):
                If True, from the center to edges of an image, gradient changes color
                from black to white; if False, from the edges to center, it does.
    """

    def __init__(self, height=256, width=256, center_h=None, center_w=None,
                 gradient_size=2, inner_to_outer=True):
        super().__init__(
            height=height,
            width=width,
            inner_color=(0, 0, 0) if inner_to_outer else (255, 255, 255),
            outer_color=(255, 255, 255) if inner_to_outer else (0, 0, 0),
            gradient_size=gradient_size,
            center_h=center_h,
            center_w=center_w
        )

    @staticmethod
    def output_image(height=256, width=256, center_h=None, center_w=None,
                     gradient_size=2, inner_to_outer=True):
        generator = RadialGradientMask(
            height=height,
            width=width,
            center_h=center_h,
            center_w=center_w,
            gradient_size=gradient_size,
            inner_to_outer=inner_to_outer
        )

        arr = generator.get_gradient_array()
        generator.output(arr, 'radial_gradient')


class TransparentRadialGradientMask(RadialGradient):
    """A class to generate black and white transparent radial gradient.
        Arges:
            height (int): The height of an image.
            width (int): The width of an image.
            center_h (int): y-axis center; must be positive; heght // 2, if not specified.
            center_w (int): x-axis center; must be positive; width // 2, if not specified.
            gradient_size (float):
                The larger the gradient_size, the smaller the circle of the gradient become.
            inner_to_outer (bool):
                If True, from the center to edges of an image, gradient changes color
                from black to transparent white; if False, from the edges to center, it does.
    """

    def __init__(self, height=256, width=256, center_h=None, center_w=None,
                 gradient_size=2, inner_to_outer=True):
        super().__init__(
            height=height,
            width=width,
            inner_color=(0, 0, 0, 255) if inner_to_outer else (255, 255, 255, 0),
            outer_color=(255, 255, 255, 0) if inner_to_outer else (0, 0, 0, 255),
            gradient_size=gradient_size,
            center_h=center_h,
            center_w=center_w
        )

    @staticmethod
    def output_image(height=256, width=256, center_h=None, center_w=None,
                     gradient_size=2, inner_to_outer=True):
        generator = TransparentRadialGradientMask(
            height=height,
            width=width,
            center_h=center_h,
            center_w=center_w,
            gradient_size=gradient_size,
            inner_to_outer=inner_to_outer
        )

        arr = generator.get_gradient_array()
        generator.output(arr, 'transparent_radial_gradient')


# if __name__ == '__main__':
    # RadialGradient.output_image()
    # RadialGradientMask.output_image()
    # TransparentRadialGradientMask.output_image()
