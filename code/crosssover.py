from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.hubs import PrimeHub
import robot


def Run(
    drive_base: DriveBase,
    left_attachment: Motor,
    right_attachment: Motor,
    hub: PrimeHub,
):
    # The main program starts here.
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=900)
    drive_base.straight(2000)
