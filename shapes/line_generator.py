import cv2

from .shape_mask import ShapeMask
from ..utils import output_image


class Lines(ShapeMask):
    """A class to draw lines on an image.
    """

    def create_lines(self, img, coordinates, color, thickness=5):
        """Draw lines on an image.
            Args:
                img (numpy.ndarray): The image onto which lines are drawn.
                coodinates (list):
                    The elements are tuples or lists containing the start and end points of the line like below.
                    [[(0, 0), (256, 256)], [(0, 128), (256, 128)], [(128, 0), (128, 256)], [(0, 256), (256, 0)]]
                color (tuple or list): Line color.
                thickness (int) Line thickness.
        """

        for start_pt, end_pt in coordinates:
            cv2.line(
                img, start_pt, end_pt, color, thickness=thickness, lineType=cv2.LINE_AA
            )

    @staticmethod
    def output_image(coordinates, bg_color, line_color, line_thickness=5,
                     height=256, width=256, gaussian_kernel=None):
        generator = Lines(bg_color, height, width)
        img = generator.create_bg_image()
        generator.create_lines(img, coordinates, line_color, line_thickness)

        if gaussian_kernel is not None:
            img = generator.blur(img, gaussian_kernel)

        # change rgb to bgr.
        img = generator.change_rgb_to_bgr(img)
        output_image(img, 'lines')


class LineMask(Lines):
    """A class to generate line mask.
        Arge:
            height (int): The height of an image; default is 256.
            width (int): The width of an image; default is 256.
            white_lines (bool):
                When True is specified, the background is black and the lines are white;
                when False is specified, the background is white and the lines are black; default is True.
    """

    def __init__(self, height=256, width=256, white_lines=True):
        super().__init__(
            bg_color=(0, 0, 0) if white_lines else (255, 255, 255),
            height=height,
            width=width
        )

        self.line_color = (255, 255, 255) if white_lines else (0, 0, 0)

    def create_lines(self, img, coordinates, thickness=5):
        super().create_lines(img, coordinates, self.line_color, thickness)

    @staticmethod
    def output_image(coordinates, line_thickness=5, height=256, width=256,
                     gaussian_kernel=31, white_lines=True):
        mask = LineMask(height, width, white_lines)
        img = mask.create_bg_image()
        mask.create_lines(img, coordinates, line_thickness)

        if gaussian_kernel is not None:
            img = mask.blur(img, gaussian_kernel)

        output_image(img, 'line_mask')


class TransparentLineMask(Lines):
    """A class to generate transparent line mask.
        Arge:
            height (int): The height of an image; default is 256.
            width (int): The width of an image; default is 256.
            white_lines (bool):
                When True is specified, the background is black and the lines are white;
                when False is specified, the background is white and the lines are black; default is True.
    """

    def __init__(self, height=256, width=256, white_lines=True):
        super().__init__(
            bg_color=(0, 0, 0, 255) if white_lines else (255, 255, 255, 255),
            height=height,
            width=width
        )

        self.line_color = (255, 255, 255, 255) if white_lines else (0, 0, 0, 255)

    def create_lines(self, img, coordinates, thickness=5):
        super().create_lines(img, coordinates, self.line_color, thickness)
        img[:, :, 3] -= img[:, :, 0]

    @staticmethod
    def output_image(coordinates, line_thickness=5, height=256, width=256,
                     gaussian_kernel=31, white_lines=True):
        mask = TransparentLineMask(height, width, white_lines)
        img = mask.create_bg_image()
        mask.create_lines(img, coordinates, line_thickness)

        if gaussian_kernel is not None:
            img = mask.blur(img, gaussian_kernel)

        output_image(img, 'trans_line_mask')