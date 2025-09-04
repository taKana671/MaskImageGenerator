import numpy as np

from .utils import output_image


class LinearGradient:
    """A class to generate gradient which direction differs for each RGB channel.
        Args:
            height (int): The height of an image.
            width (int): The width of an image.
            start_color: (tuple or list):
                The starting color of gradient; values ranging from 0 to 255;
                the number of elements must be the same as end_color.
            end_color (tuple or list):
                The end color of gradient; values ranging from 0 to 255;
                the number of elements must be the same as start_color.
            is_horizontal (tuple or list):
                Specify the gradient direction for each RGB channel; set to True for horizontal, False for vertical;
                the number of elements must be the same as start_color and end_color.
    """

    def __init__(self, height, width, start_color, end_color, is_horizontal):
        self.height = height
        self.width = width
        self.start_color = start_color
        self.end_color = end_color
        self.is_horizontal = is_horizontal

    def get_gradient_2d(self, start, stop, is_horizontal):
        if is_horizontal:
            return np.tile(np.linspace(start, stop, self.width), (self.height, 1))

        return np.tile(np.linspace(start, stop, self.height), (self.width, 1)).T

    def get_gradient_3d(self):
        arr = np.zeros((self.height, self.width, len(self.is_horizontal)), dtype=np.uint8)

        for i, (start, stop, is_hor) in enumerate(
                zip(self.start_color, self.end_color, self.is_horizontal)):
            arr[:, :, i] = self.get_gradient_2d(start, stop, is_hor)

        return arr

    @staticmethod
    def output_image(height, width, start_color, end_color, is_horizontal):
        generator = LinearGradient(height, width, start_color, end_color, is_horizontal)
        arr = generator.get_gradient_3d()
        output_image(arr, 'linear_gradient')


class HorizontalGradientMask(LinearGradient):
    """A class to generate black and white horizontal gradient.
        Args:
            height (int): The height of an image.
            width (int): The width of an image.
            left_to_right (bool):
                If True, from the left to right of an image, gradient changes color
                from black to white; if False, from the right to left, it does.
    """

    def __init__(self, height=256, width=256, left_to_right=True):
        super().__init__(
            height=height,
            width=width,
            start_color=(0, 0, 0) if left_to_right else (255, 255, 255),
            end_color=(255, 255, 255) if left_to_right else (0, 0, 0),
            is_horizontal=(True, True, True)
        )

    @staticmethod
    def output_image(height=256, width=256, left_to_right=True):
        generator = HorizontalGradientMask(height, width, left_to_right)
        arr = generator.get_gradient_3d()
        output_image(arr, 'horizontal_gradient')


class TransparentHorizontalGradientMask(LinearGradient):
    """A class to generate black and white transparent horizontal gradient.
        Args:
            height (int): The height of an image.
            width (int): The width of an image.
            left_to_right (bool):
                If True, from the left to right of an image, gradient changes color
                from black to transparent white; if False, from the right to left, it does.
    """

    def __init__(self, height=256, width=256, left_to_right=True):
        super().__init__(
            height=height,
            width=width,
            start_color=(0, 0, 0, 255) if left_to_right else (255, 255, 255, 0),
            end_color=(255, 255, 255, 0) if left_to_right else (0, 0, 0, 255),
            is_horizontal=(True, True, True, True)
        )

    @staticmethod
    def output_image(height=256, width=256, left_to_right=True):
        generator = TransparentHorizontalGradientMask(height, width, left_to_right)
        arr = generator.get_gradient_3d()
        output_image(arr, 'trans_horizontal_gradient')


class VerticalGradientMask(LinearGradient):
    """A class to generate black and white vertical gradient.
        Args:
            height (int): The height of an image.
            width (int): The width of an image.
            top_to_bottom (bool):
                If True, from the top to bottom of an image, gradient changes color
                from black to white; if False, from the bottom to top, it does.
    """

    def __init__(self, height=256, width=256, top_to_bottom=True):
        super().__init__(
            height=height,
            width=width,
            start_color=(0, 0, 0) if top_to_bottom else (255, 255, 255),
            end_color=(255, 255, 255) if top_to_bottom else (0, 0, 0),
            is_horizontal=(False, False, False)
        )

    @staticmethod
    def output_image(height=256, width=256, top_to_bottom=True):
        generator = VerticalGradientMask(height, width, top_to_bottom)
        arr = generator.get_gradient_3d()
        output_image(arr, 'vertical_gradient')


class TransparentVerticalGradientMask(LinearGradient):
    """A class to generate black and white transparent vertical gradient.
        Args:
            height (int): The height of an image.
            width (int): The width of an image.
            top_to_bottom (bool):
                If True, from the top to bottom of an image, gradient changes color
                from black to transparent white; if False, from the bottom to top, it does.
    """

    def __init__(self, height=256, width=256, top_to_bottom=True):
        super().__init__(
            height=height,
            width=width,
            start_color=(0, 0, 0, 255) if top_to_bottom else (255, 255, 255, 0),
            end_color=(255, 255, 255, 0) if top_to_bottom else (0, 0, 0, 255),
            is_horizontal=(False, False, False, False)
        )

    @staticmethod
    def output_image(height=256, width=256, top_to_bottom=True):
        generator = TransparentVerticalGradientMask(height, width, top_to_bottom)
        arr = generator.get_gradient_3d()
        output_image(arr, 'trans_vertical_gradient')


# if __name__ == '__main__':
#     HorizontalGradientMask.output_image()
#     TransparentHorizontalGradientMask.output_image()
#     VerticalGradientMask.output_image()
#     TransparentVerticalGradientMask.output_image()