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
    # The main program starts here.
    drive_base.use_gyro(True)
    drive_base.straight(585)
    drive_base.turn(-90)
    drive_base.turn(90)
    drive_base.straight(-585)


# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    robot = robot.Robot()
    Run(
        robot.drive_base,
        robot.left_attachment,
        robot.right_attachment,
        robot.hub,
    )
