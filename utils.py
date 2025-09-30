from datetime import datetime

import cv2


def output_image(arr, stem, output_dir=None, with_suffix=True):
    if with_suffix:
        now = datetime.now()
        stem = f'{stem}_{now.strftime("%Y%m%d%H%M%S")}'

    output_file = f'{stem}.png'

    if output_dir is not None:
        output_file = f'{output_dir}/{output_file}'

    cv2.imwrite(output_file, arr)