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


```bash
from radial_gradient_generator import RadialGradientMask, TransparentRadialGradientMask

RadialGradientMask.output_image()
TransparentRadialGradientMask.output_image()

# if you want only numpy.ndarray of the image
# generator = RadialGradientMask()
# arr = generator.get_gradient_array()
```
