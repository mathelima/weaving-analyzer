import time

from hardware_controllers.cameras_controller.enumerators import LightType
from src.camera_manager import CameraManager
from src.request_manager import RequestManager
from src.velocity_manager import VelocityManager
from utils.logger import Logger

logger = Logger("main")


def main():
    # Initialize managers
    velocity_manager = VelocityManager(update_frequency=10, window_size=10)
    camera_manager = CameraManager()
    request_manager = RequestManager(base_url="http://127.0.0.1:5000")

    try:
        # Start velocity sensor
        velocity_manager.start()
        logger.info("Velocity sensor started.")

        while True:
            # Get current displacement
            displacement = velocity_manager.get_displacement()

            # Capture images if displacement threshold is met
            images_green = camera_manager.capture_images(LightType.GREEN)
            images_blue = camera_manager.capture_images(LightType.BLUE)
            logger.info("Captured images.")

            # Send velocity and displacement to the server
            velocity = velocity_manager._filter.update(
                velocity_manager._sensor.get_velocity()
            )
            request_manager.send_surface_movement(velocity, displacement)
            logger.info(
                f"Sent velocity: {velocity} cm/min, displacement: {displacement} cm."
            )

            # Send captured images to the server
            request_manager.send_pictures_batch({"images": [images_green, images_blue]})
            logger.info("Sent images batch to the server.")

            # Wait for the next cycle
            time.sleep(1)

    except KeyboardInterrupt:
        logger.warning("Shutting down...")
    finally:
        velocity_manager.stop()
        logger.info("Velocity sensor stopped.")


if __name__ == "__main__":
    main()
