from datetime import datetime

import numpy as np
import cv2


def output_image(arr, img_type, output_dir=None):
    output_file = f'{img_type}_{datetime.now().strftime("%Y%m%d%H%M%S")}.png'

    if output_dir is not None:
        output_file = f'{output_dir}/{output_file}'

    arr = np.clip(arr * 255, a_min=0, a_max=255).astype(np.uint8)
    cv2.imwrite(output_file, arr)