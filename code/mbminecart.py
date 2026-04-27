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
    # Outside of left wheel on 8
    # Rear of robot lined up with thin black line
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=900)
    drive_base.straight(730)
    drive_base.turn(70)
    drive_base.straight(213)
    left_attachment.run_angle(450, 160)
    wait(1000)
    left_attachment.run_angle(450, -160)
    drive_base.straight(-213)
    drive_base.turn(-118)
    drive_base.straight(180)
    drive_base.straight(-200)
    drive_base.turn(70)
    drive_base.straight(-900)


# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    robot = robot.Robot()
    Run(
        robot.drive_base,
        robot.left_attachment,
        robot.right_attachment,
        robot.hub,
    )
