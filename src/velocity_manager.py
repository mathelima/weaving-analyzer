import threading
import time

from hardware_controllers.velocity_sensor_controller import VelocitySensorController  # noqa: E501
from utils.moving_average import MovingAverage


class VelocityManager:
    """
    Manages velocity and displacement calculations using a simulated velocity sensor.

    This class provides methods to start and stop the sensor, as well as retrieve displacement data.
    """  # noqa: E501

    def __init__(self, update_frequency=10, window_size=10):
        self._sensor = VelocitySensorController()
        self._filter = MovingAverage(window_size)
        self._update_frequency = update_frequency
        self._displacement = 0
        self._running = False
        self._lock = threading.Lock()

    def start(self):
        """
        Start the velocity sensor to begin collecting data.
        """
        self._running = True
        self._sensor.start_sensor()
        threading.Thread(target=self._run, daemon=True).start()

    def stop(self):
        """
        Stop the velocity sensor to stop data collection.
        """
        self._running = False
        self._sensor.stop_sensor()

    def get_displacement(self):
        """
        Returns the current displacement value from the velocity sensor.
        """
        with self._lock:
            return self._displacement

    def _run(self):
        while self._running:
            velocity = self._sensor.get_velocity()
            filtered_velocity = self._filter.update(max(velocity, 0))
            with self._lock:
                self._displacement += (
                    filtered_velocity / 60 / self._update_frequency
                )
            time.sleep(1 / self._update_frequency)
