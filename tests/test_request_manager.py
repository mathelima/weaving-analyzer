from unittest.mock import MagicMock, patch

import pytest

from src.request_manager import RequestManager


@pytest.fixture
def request_manager():
    return RequestManager("http://localhost:5000")


@patch("src.request_manager.requests.post")
def test_send_velocity_data(mock_post, request_manager):
    # given
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_post.return_value = mock_response

    # when
    request_manager.send_surface_movement(velocity=10.0, displacement=5.0)

    # then
    mock_post.assert_called_once_with(
        "http://localhost:5000/surface_movement",
        json={"velocity": 10.0, "displacement": 5.0},
    )
    mock_response.raise_for_status.assert_called_once()


@patch("src.request_manager.requests.post")
def test_send_pictures_batch(mock_post, request_manager):
    # given
    mock_response = MagicMock()
    mock_response.raise_for_status = MagicMock()
    mock_post.return_value = mock_response

    # when
    request_manager.send_pictures_batch(batch=["image1", "image2"])

    # then
    mock_post.assert_called_once_with(
        "http://localhost:5000/pictures_batch", data='["image1", "image2"]'
    )
    mock_response.raise_for_status.assert_called_once()
