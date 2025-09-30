import cv2

from .shape_mask import ShapeMask
from ..utils import output_image


class Circles(ShapeMask):
    """A class to draw a circle on an image.
    """

    def create_circle(self, img, color, radius, thickness=-1, center=None):
        """Draw a circle.
            Args:
                img (numpy.ndarray): The image onto which circle is drawn.
                color (tuple or list): The color of the circle.
                radius (int): The radius of the circle.
                thickness (int): Line thickness; Setting a negative value draws a filled circle; default is -1.
                center (tuple): Specify the center coordinates as a tuple (x, y);
                                the coordinate values must be integers; if None is specified,
                                the center is (width / 2, height / 2); default is None.
        """
        if center is None:
            center = (int(self.width / 2), int(self.height / 2))

        cv2.circle(img, center, radius, color, thickness, cv2.LINE_AA)

    @staticmethod
    def output_image(bg_color, circlr_color, height=256, width=256, radius=50,
                     thickness=-1, circle_center=None, gaussian_kernel=None,
                     output_dir=None, with_suffix=True):
        generator = Circles(bg_color, height, width)
        img = generator.create_bg_image()
        generator.create_circle(img, circlr_color, radius, thickness, circle_center)

        if gaussian_kernel is not None:
            img = generator.blur(img, gaussian_kernel)

        # change rgb to bgr.
        img = generator.change_rgb_to_bgr(img)
        output_image(img, 'circle', output_dir, with_suffix)


class CircleMask(Circles):
    """A class to generate a circle mask.
        Arge:
            height (int): The height of an image; default is 256.
            width (int): The width of an image; default is 256.
            white_circle (bool):
                When True is specified, the background is black and the circle is white;
                when False is specified, the background is white and the circle is black; default is True.
    """

    def __init__(self, height=256, width=256, white_circle=True):
        super().__init__(
            bg_color=(0, 0, 0) if white_circle else (255, 255, 255),
            height=height,
            width=width
        )

        self.circle_color = (255, 255, 255) if white_circle else (0, 0, 0)

    def create_circle(self, img, radius, thickness=-1, center=None):
        super().create_circle(img, self.circle_color, radius, thickness, center)

    @staticmethod
    def output_image(height=256, width=256, radius=50, thickness=-1,
                     circle_center=None, gaussian_kernel=51, white_circle=True,
                     output_dir=None, with_suffix=True):
        generator = CircleMask(height, width, white_circle)
        img = generator.create_bg_image()
        generator.create_circle(img, radius, thickness, circle_center)

        if gaussian_kernel is not None:
            img = generator.blur(img, gaussian_kernel)

        output_image(img, 'circle_mask', output_dir, with_suffix)


class TransparentCircleMask(Circles):
    """A class to generate transparent circle mask.
        Arge:
            height (int): The height of an image; default is 256.
            width (int): The width of an image; default is 256.
            white_circle (bool):
                When True is specified, the background is black and the circle is white;
                when False is specified, the background is white and the circle is black; default is True.
    """

    def __init__(self, height=256, width=256, white_circle=True):
        super().__init__(
            bg_color=(0, 0, 0, 255) if white_circle else (255, 255, 255, 255),
            height=height,
            width=width
        )

        self.circle_color = (255, 255, 255, 255) if white_circle else (0, 0, 0, 255)

    def create_circle(self, img, radius, thickness=-1, center=None):
        super().create_circle(img, self.circle_color, radius, thickness, center)
        img[:, :, 3] -= img[:, :, 0]

    @staticmethod
    def output_image(height=256, width=256, radius=50, thickness=-1, circle_center=None,
                     gaussian_kernel=51, white_circle=True,
                     output_dir=None, with_suffix=True):
        generator = TransparentCircleMask(height, width, white_circle)
        img = generator.create_bg_image()
        generator.create_circle(img, radius, thickness, circle_center)

        if gaussian_kernel is not None:
            img = generator.blur(img, gaussian_kernel)

        output_image(img, 'trans_circle_mask', output_dir, with_suffix)
