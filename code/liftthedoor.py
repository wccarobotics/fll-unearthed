from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
from pybricks.tools import wait
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
    drive_base.straight(350)
    drive_base.turn(-45)
    drive_base.turn(32)
    drive_base.straight(270)
    drive_base.straight(-250)
    drive_base.straight(100)
    drive_base.turn(75)
    drive_base.straight(-200)
    drive_base.turn(75)
    drive_base.straight(500)


# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    robot = robot.Robot()
    Run(
        robot.drive_base,
        robot.left_attachment,
        robot.right_attachment,
        robot.hub,
    )
