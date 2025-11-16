from unittest.mock import MagicMock

import pytest

from src.velocity_manager import VelocityManager


@pytest.fixture
def velocity_manager():
    return VelocityManager(update_frequency=10, window_size=10)


def test_start(velocity_manager):
    # given
    velocity_manager._sensor = MagicMock()
    velocity_manager._sensor.start = MagicMock()

    # when
    velocity_manager.start()

    # then
    assert velocity_manager._running is True
    velocity_manager._sensor.start_sensor.assert_called_once()


def test_stop(velocity_manager):
    # given
    velocity_manager._sensor = MagicMock()
    velocity_manager._sensor.stop = MagicMock()

    # when
    velocity_manager.stop()

    # then
    assert velocity_manager._running is False
    velocity_manager._sensor.stop_sensor.assert_called_once()


def test_get_displacement(velocity_manager):
    # given
    velocity_manager._displacement = 15.0

    # when
    displacement = velocity_manager.get_displacement()

    # then
    assert displacement == 15.0
