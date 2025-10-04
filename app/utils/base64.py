
import base64
import numpy as np
import cv2


def base64_to_image(base64_string: str):
    try:
        img_data = base64.b64decode(base64_string)
        np_arr = np.frombuffer(img_data, np.uint8)
        return cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    except Exception as e:
        raise ValueError("Invalid base64 string") from e
