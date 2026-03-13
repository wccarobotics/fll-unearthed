from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
import robot


def Run(
    drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor
):
    # The main program starts here.
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=900)
    drive_base.straight(2000)
