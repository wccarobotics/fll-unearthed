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
    # Starting Position: Back of the robot on the back line with the left
    # wheel aligned nine inches from the right edge of the mat.
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=900)
    drive_base.straight(785)
    drive_base.turn(-45)
    drive_base.straight(50)
    drive_base.turn(-45)
    drive_base.turn(75, then=Stop.NONE)
    drive_base.straight(-735, then=Stop.NONE)
    drive_base.straight(-300, then=Stop.NONE)
    left_attachment.run_angle(90, 90, then=Stop.HOLD, wait=False)


# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    robot = robot.Robot()
    Run(
        robot.drive_base,
        robot.left_attachment,
        robot.right_attachment,
        robot.hub,
    )
