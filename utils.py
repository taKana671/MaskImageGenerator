from datetime import datetime

import cv2


def output_image(arr, img_type, output_dir=None):
    output_file = f'{img_type}_{datetime.now().strftime("%Y%m%d%H%M%S")}.png'

    if output_dir is not None:
        output_file = f'{output_dir}/{output_file}'

    cv2.imwrite(output_file, arr)