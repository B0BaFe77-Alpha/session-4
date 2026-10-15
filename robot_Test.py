import pytest
from robot import RobotBase


@pytest.fixture
def robot():
    return RobotBase(
        "Robo1",
        100,
        False,
        {
            "temperature": 25,
            "distance": 10
        }
    )


# -------------------------
# INITIALISATION TESTS
# -------------------------

def test_robot_initialises_correctly(robot):
    assert robot._name == "Robo1"
    assert robot._battery_level == 100
    assert robot._is_moving is False
    assert robot._sensor_readings == {
        "temperature": 25,
        "distance": 10
    }


# -------------------------
# PROPERTY TESTS
# -------------------------

def test_name(robot):
    assert robot.name == "Robo1"


def test_battery_level(robot):
    assert robot.battery_level == 100


def test_is_moving(robot):
    assert robot.is_moving is False


def test_sensor_readings(robot):
    assert robot.sensor_readings == {
        "temperature": 25,
        "distance": 10
    }


# -------------------------
# BATTERY TESTS
# -------------------------

def test_battery_can_be_changed(robot):
    robot.battery_level = 50

    assert robot.battery_level == 50


def test_battery_cannot_be_negative(robot):
    with pytest.raises(ValueError):
        robot.battery_level = -1


def test_battery_can_be_zero(robot):
    robot.battery_level = 0

    assert robot.battery_level == 0


# -------------------------
# MOVEMENT TESTS
# -------------------------

def test_move_forward_returns_speed(robot):
    result = robot.move_forward(5)

    assert result == 5


def test_move_forward_rejects_negative_speed(robot):
    with pytest.raises(ValueError):
        robot.move_forward(-5)


def test_move_forward_with_zero_speed(robot):
    with pytest.raises(ValueError):
        robot.move_forward(0)


def test_robot_stops_when_battery_is_empty(robot):
    robot.battery_level = 0

    robot.move_forward(5)

    assert robot.is_moving is False


# -------------------------
# STOP TEST
# -------------------------

def test_stop(robot):
    robot._is_moving = True

    robot.stop()

    assert robot.is_moving is False


# -------------------------
# SENSOR TESTS
# -------------------------

def test_get_temperature_sensor(robot):
    result = robot.get_sensor_reading("temperature")

    assert result == 25


def test_get_distance_sensor(robot):
    result = robot.get_sensor_reading("distance")

    assert result == 10


def test_get_sensor_that_does_not_exist(robot):
    with pytest.raises(ValueError):
        robot.get_sensor_reading("camera")


def test_change_sensor_reading(robot):
    robot.set_sensor_reading("temperature", 30)

    assert robot.get_sensor_reading("temperature") == 30


def test_change_sensor_that_does_not_exist(robot):
    with pytest.raises(ValueError):
        robot.set_sensor_reading("camera", 50)


# -------------------------
# REPORT STATUS TEST
# -------------------------

def test_report_status(robot):
    result = robot.report_status()

    assert "Robo1" in result
    assert "100" in result
    assert "False" in result
    assert "temperature" in result
    assert "distance" in result