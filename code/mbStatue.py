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
    drive_base.straight(650)
    drive_base.turn(-45)
    drive_base.straight(50)
    drive_base.turn(45)
    drive_base.straight(345)
    drive_base.turn(-135)
    drive_base.straight(248)
    left_attachment.run_angle(150, 90, Stop.NONE)
    drive_base.turn(30)
    left_attachment.stop()
    drive_base.turn(-30)
    drive_base.straight(-200)
    drive_base.turn(45)
    drive_base.straight(-230)
    for count in range(2):
        drive_base.turn(-7)
        right_attachment.run_angle(500, 1080, Stop.NONE)
    drive_base.straight(5)
    drive_base.straight(200)
    drive_base.turn(-85)
    drive_base.straight(950)


# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    robot = robot.Robot()
    Run(
        robot.drive_base,
        robot.left_attachment,
        robot.right_attachment,
        robot.hub,
    )
