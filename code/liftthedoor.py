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
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=600)
    drive_base.straight(365)
    drive_base.turn(-35)
    drive_base.straight(-100)
    drive_base.turn(25)
    drive_base.straight(350)
    drive_base.straight(-250)
    drive_base.straight(100)
    drive_base.turn(80)
    drive_base.straight(-200)
    drive_base.turn(65)
    drive_base.straight(-1100)
    drive_base.arc(100, angle=-45)
    drive_base.straight(-500)


# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    robot = robot.Robot()
    Run(
        robot.drive_base,
        robot.left_attachment,
        robot.right_attachment,
        robot.hub,
    )
