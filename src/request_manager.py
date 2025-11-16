import base64
import json
from io import BytesIO

import numpy as np
import requests
from PIL import Image

from utils.logger import Logger

logger = Logger("request_manager")


class RequestManager:
    """
    Handles communication with the server, including sending
    surface movement data and batches of pictures.
    """

    def __init__(self, base_url):
        self._base_url = base_url

    def send_surface_movement(self, velocity, displacement):
        """
        Send surface movement data (velocity and displacement) to the server.
        """
        url = f"{self._base_url}/surface_movement"
        data = {"velocity": velocity, "displacement": displacement}
        try:
            response = requests.post(url, json=data)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Failed to send surface movement data: {e}")

    def send_pictures_batch(self, batch):
        """
        Send a batch of pictures to the server.

        The batch may contain NumPy arrays representing images, which are
        converted to Base64 strings before being sent.
        """
        url = f"{self._base_url}/pictures_batch"

        def encode_images(obj):
            if isinstance(obj, np.ndarray):
                image = Image.fromarray(obj)
                buffer = BytesIO()
                image.save(buffer, format="JPEG")
                return base64.b64encode(buffer.getvalue()).decode("utf-8")
            raise TypeError(f"Object of type {type(obj)} is not JSON serializable")  # noqa: E501

        try:
            data = json.dumps(batch, default=encode_images)
            response = requests.post(url, data=data)
            response.raise_for_status()
        except requests.RequestException as e:
            logger.error(f"Failed to send pictures batch: {e}")
