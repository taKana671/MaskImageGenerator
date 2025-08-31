# MaskImageGenerator

This is a repository for creating mask images. Mask images can be used when processing noise.

# Requirements

* numpy 2.2.4
* opencv-contrib-python 4.11.0.86
* opencv-python 4.11.0.86

# Environment

* Python 3.12
* Windows11

# Radial Gradient

![demo1](https://github.com/user-attachments/assets/e6adfb43-f453-4705-9e24-108ceb8e96c5)

```bash
from radial_gradient_generator import RadialGradientMask, TransparentRadialGradientMask

RadialGradientMask.output_image()
TransparentRadialGradientMask.output_image()

# if you want only numpy.ndarray of the image
# generator = RadialGradientMask()
# arr = generator.get_gradient_array()
```

### parameters

* _height: int_
    * The height of an image; default is 256.

* _width: int_
    * The width of an image; default is 256.

* _center_h: int_
    * y-axis center; must be positive; heght // 2, if not specified.

* _center_w: int_
    * x-axis center; must be positive; width // 2, if not specified.

* _gradient_size: float_
    * The larger the gradient_size, the smaller the circle of the gradient become; default is 2.0.
            
* _inner_to_outer: bool_
    * If True, from the center to edges of an image, gradient changes color from black to white; if False, from the edges to center, it does; default is True.

# Horizontal Gradient

![demo2](https://github.com/user-attachments/assets/ac2cb432-d8ed-4f16-a67f-21ed3c54f597)

```bash
from linear_gradient_generator import HorizontalGradientMask, TransparentHorizontalGradientMask

HorizontalGradientMask.output_image()
TransparentHorizontalGradientMask.output_image()

# if you want only numpy.ndarray of the image
# generator = HorizontalGradientMask()
# arr = generator.get_gradient_3d()
```

### parameters

* _height: int_
    * The height of an image; default is 256.

* _width: int_
    * The width of an image; default is 256.

* _left_to_right: bool_
    * If True, from the left to right of an image, gradient changes color from black to white; if False, from the right to left, it does; default is True.

# Vertical Gradient

![demo3](https://github.com/user-attachments/assets/4c8b1ef5-51f4-435b-aeef-a7a94f4d0e39)

```bash
from linear_gradient_generator import VerticalGradientMask, TransparentVerticalGradientMask

VerticalGradientMask.output_image()
TransparentVerticalGradientMask.output_image()

# if you want only numpy.ndarray of the image
# generator = VerticalGradientMask()
# arr = generator.get_gradient_3d()
```

### parameters

height (int): The height of an image.
            width (int): The width of an image.
            left_to_right (bool):
                If True, from the left to right of an image, gradient changes color
                from black to white; if False, from the right to left, it does.

* _height: int_
    * The height of an image; default is 256.

* _width: int_
    * The width of an image; default is 256.

* _left_to_right: bool_
    * If True, from the top to bottom of an image, gradient changes color from black to white; if False, from the bottom to top, it does; default is True.

