from pybricks.parameters import Direction, Port, Stop
from pybricks.pupdevices import Motor
from pybricks.robotics import DriveBase
import robot


def Run(
    drive_base: DriveBase, left_attachment: Motor, right_attachment: Motor
):
    # The main program starts here.
    drive_base.use_gyro(True)
    drive_base.settings(straight_speed=400)
    drive_base.straight(600)
    drive_base.turn(-90)
    drive_base.straight(250)
    drive_base.straight(-200)


# This code allows this program to be run directly, without the main program
if __name__ == "__main__":
    robot = robot.Robot()
    Run(robot.drive_base, robot.left_attachment, robot.right_attachment)
