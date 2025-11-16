from unittest.mock import MagicMock, patch

import pytest

from hardware_controllers.cameras_controller.enumerators import LightType
from src.camera_manager import CameraManager


@pytest.fixture
def mock_cameras_controller():
    with patch("src.camera_manager.CamerasController") as MockController:
        mock_controller = MockController.return_value
        mock_controller.open_cameras = MagicMock()
        mock_controller.set_light_type = MagicMock()
        mock_controller.trigger = MagicMock()
        mock_controller.collect_pictures = MagicMock(return_value=["image1", "image2"])  # noqa: E501
        yield mock_controller


@pytest.fixture
def camera_manager(mock_cameras_controller):
    return CameraManager()


def test_capture_images(camera_manager, mock_cameras_controller):
    # given
    light_type = LightType.GREEN

    # when
    images = camera_manager.capture_images(light_type)

    # then
    mock_cameras_controller.set_light_type.assert_called_once_with(light_type)
    mock_cameras_controller.trigger.assert_called_once()
    mock_cameras_controller.collect_pictures.assert_called_once_with(light_type)  # noqa: E501
    assert images == ["image1", "image2"]
