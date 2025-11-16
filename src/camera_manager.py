from threading import Lock

from hardware_controllers.cameras_controller.cameras_controller import CamerasController  # noqa: E501


class CameraManager:
    """
    Manages camera operations, including triggering and capturing images
    with specific lighting.
    """

    def __init__(self):
        self._controller = CamerasController()
        self._controller.open_cameras()
        self._lock = Lock()

    def capture_images(self, light_type):
        """
        Capture images using the cameras with the specified light type.
        """
        with self._lock:
            self._controller.set_light_type(light_type)
            self._controller.trigger()
            return self._controller.collect_pictures(light_type)
